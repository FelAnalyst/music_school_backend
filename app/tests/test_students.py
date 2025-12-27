# app/tests/test_students.py

from app.services.students.service import get_students
from app.services.students.schemas import StudentFilter

def test_students():
    students = get_students(StudentFilter())
    print(students)

test_students()
