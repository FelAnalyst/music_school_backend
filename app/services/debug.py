from app.services.students.service import get_students, get_student_lessons
from app.services.students.schemas import StudentFilter, StudentLessonFilter


def debug_students(**kwargs):
    print("=== DEBUG STUDENTS ===")
    filters = StudentLessonFilter(**kwargs)
    result = get_student_lessons(filters)
    for row in result:
        print(row)
    print(f"Total: {len(result)}\n")

if __name__ == "__main__":
    debug_students(last_name="Джексон", date_from = '2025-10-01', date_to = '2025-10-20')
