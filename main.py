from fastapi import FastAPI, HTTPException
from typing import List

from models import Student, StudentCreate
from student_store import students
from ollama_client import generate_summary

app = FastAPI(title="FealtyX Backend Assignment", version="1.0.0")


@app.post("/students", response_model=Student, status_code=201)
def create_student(student: StudentCreate):
    """Create a new student and return the record with an auto-generated ID."""
    # Check for duplicate email
    for s in students.values():
        if s.email == student.email:
            raise HTTPException(status_code=400, detail="Student with this email already exists")
        
    new_id = max(students.keys(), default=0) + 1
    new_student = Student(id=new_id, **student.model_dump())
    students[new_id] = new_student
    return new_student

@app.get("/students", response_model=List[Student])
def list_students():
    """Return all students in the store."""
    return list(students.values())


@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
    """Return a single student by ID."""
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return students[student_id]


@app.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, data: StudentCreate):
    """Completely update a student (overwrite all fields)."""
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    
    # Prevent duplicate emails during update (ignore current student)
    for sid, s in students.items():
        if sid != student_id and s.email == data.email:
            raise HTTPException(status_code=400, detail="Another student with this email already exists")
        
    updated = Student(id=student_id, **data.model_dump())
    students[student_id] = updated
    return updated


@app.delete("/students/{student_id}", status_code=204)
def delete_student(student_id: int):
    """Delete a student record."""
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    del students[student_id]
    return None


@app.get("/students/{student_id}/summary")
async def student_summary(student_id: int):
    """Generate an AI summary for a student using local Ollama."""
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    summary = await generate_summary(students[student_id])
    return {"summary": summary}




