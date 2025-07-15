"""In-memory store for Student objects."""
from typing import Dict
from models import Student

students: Dict[int, Student] = {}