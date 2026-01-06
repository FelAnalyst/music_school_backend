import pandas as pd
from app.services.finance.schemas import FinancePeriodFilter
from app.services.finance.queries import (
    LESSONS_BY_STUDENT,
    STUDENT_BALANCES,
    PAYMENTS_AGGREGATED,
)
from app.services.finance.service import _fetch_with_columns

def print_table(rows, columns, title: str):
    print(f"\n--- {title} ---")
    if not rows:
        print("No data")
        return
    df = pd.DataFrame(rows, columns=columns)
    print(df)


def debug_finance(**kwargs):
    filters = FinancePeriodFilter(**kwargs)
    params = filters.model_dump()

    rows, cols = _fetch_with_columns(LESSONS_BY_STUDENT, params)
    print_table(rows, cols, "LESSONS BY STUDENT")

    rows, cols = _fetch_with_columns(STUDENT_BALANCES, params)
    print_table(rows, cols, "STUDENT BALANCES")

    rows, cols = _fetch_with_columns(PAYMENTS_AGGREGATED, params)
    print_table(rows, cols, "PAYMENTS AGGREGATED")


if __name__ == "__main__":
    debug_finance(student_id=5, date_from = '2025-09-01', date_to = '2025-12-20')
