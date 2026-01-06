from app.db import get_connection
from app.services.finance.schemas import FinancePeriodFilter
from app.services.finance.queries import (
    LESSONS_BY_STUDENT,
    STUDENT_BALANCES,
    PAYMENTS_AGGREGATED,
)

def _fetch_all(sql: str, params: dict):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, params)
            return cur.fetchall()


def _fetch_with_columns(sql: str, params: dict):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, params)
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            return rows, columns


def lessons_by_student(filters: FinancePeriodFilter):
    return _fetch_all(LESSONS_BY_STUDENT, filters.model_dump())


def student_balances(filters: FinancePeriodFilter):
    return _fetch_all(STUDENT_BALANCES, filters.model_dump())


def payments_aggregated(filters: FinancePeriodFilter):
    return _fetch_all(PAYMENTS_AGGREGATED, filters.model_dump())