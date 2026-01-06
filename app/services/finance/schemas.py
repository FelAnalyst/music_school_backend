from pydantic import BaseModel
from datetime import date

class FinancePeriodFilter(BaseModel):
    student_id: int | None = None
    date_from: date | None = None
    date_to: date | None = None

