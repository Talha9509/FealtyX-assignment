# """Asynchronous helper to query the local Ollama server."""
import httpx
from models import Student
import asyncio

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"  # Default Ollama endpoint
OLLAMA_MODEL = "llama3.2"  # Change if you prefer another local model

async def generate_summary(student: Student) -> str:
    """Return a short AI‑generated profile summary for a Student."""
    
    prompt = (
    "I am a Science Teacher in Newton high School. Help me in managing the data of students. So Generate a professional summary for a fictional student based on the following details:\n"
    f"Name: {student.name}\n"
    f"Age: {student.age}\n"
    f"Email: {student.email}\n"
    "The summary should be 3-4 concise sentences and suitable for a student profile page."
    )

    


    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
    }

        

    async with httpx.AsyncClient() as client:
        try:
            resp = await client.post(OLLAMA_URL, json=payload)
            if resp.status_code == 200:
                print(resp.json())  
                return resp.json().get("response", " response from Ollama")

            else:
                return f"Error generating the summary: {resp.text}"
        except Exception as exc:
            return f"Error generating summary: {exc}"
 