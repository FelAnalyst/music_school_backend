from app.db import get_connection
from app.services.finance.queries import LESSONS_BY_STUDENT

def lessons_by_student(filters):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(LESSONS_BY_STUDENT, filters.model_dump())
            return cur.fetchall()
