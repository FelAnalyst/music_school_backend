# app/services/students/service.py
from psycopg2.extras import RealDictCursor
from app.services.students.schemas import StudentFilter, StudentLessonFilter
from app.db import get_connection
from app.services.students.queries import (STUDENTS_WITHOUT_LESSONS, BASE_STUDENTS_QUERY,
                                           BASE_STUDENT_LESSONS_SQL)

def get_students_without_lessons():
    with get_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(STUDENTS_WITHOUT_LESSONS)
            return cur.fetchall()

def get_students(filters: StudentFilter):
    sql = BASE_STUDENTS_QUERY
    params = {}

    if filters.first_name:
        sql += " AND st.first_name ILIKE %(first_name)s"
        params["first_name"] = f"%{filters.first_name}%"

    if filters.last_name:
        sql += " AND st.last_name ILIKE %(last_name)s"
        params["last_name"] = f"%{filters.last_name}%"

    with get_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(sql, params)
            return cur.fetchall()

def get_student_lessons(filters: StudentLessonFilter):
    where_clauses = []
    params = {}

    if filters.first_name:
        where_clauses.append("s.first_name = %(first_name)s")
        params["first_name"] = filters.first_name

    if filters.last_name:
        where_clauses.append("s.last_name = %(last_name)s")
        params["last_name"] = filters.last_name

    if filters.subject_name:
        where_clauses.append("sub.subject_name = %(subject_name)s")
        params["subject_name"] = filters.subject_name

    if filters.date_from:
        where_clauses.append("lst.date >= %(date_from)s")
        params["date_from"] = filters.date_from

    if filters.date_to:
        where_clauses.append("lst.date <= %(date_to)s")
        params["date_to"] = filters.date_to

    sql = BASE_STUDENT_LESSONS_SQL
    if where_clauses:
        sql += " WHERE " + " AND ".join(where_clauses)

    with get_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(sql, params)
            return cur.fetchall()