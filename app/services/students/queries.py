# app/services/students/queries.py

STUDENTS_WITHOUT_LESSONS = """
SELECT st.*
FROM students st
WHERE NOT EXISTS (
    SELECT 1
    FROM lesson_students ls
    WHERE ls.student_id = st.student_id
)
"""

BASE_STUDENTS_QUERY = """
SELECT st.*
FROM students st
WHERE 1=1
"""

BASE_STUDENT_LESSONS_SQL = """
SELECT lst.*
FROM lessons_student_total_info lst
JOIN students s ON s.student_id = lst.student_id
JOIN subjects sub ON sub.subject_id = lst.subject_id
"""

