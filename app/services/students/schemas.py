from pydantic import BaseModel
from datetime import date
from typing import Optional

class StudentFilter(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    date_from: date | None = None
    date_to: date | None = None
    subject: str | None = None

class StudentLessonFilter(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    subject_name: Optional[str] = None
    date_from: Optional[date] = None
    date_to: Optional[date] = None
