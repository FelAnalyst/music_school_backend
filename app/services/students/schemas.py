from datetime import date
from typing import Optional


class StudentFilter():
    first_name: str | None = None
    last_name: str | None = None
    #date_from: date | None = None
    #date_to: date | None = None
    #subject: int | None = None

class StudentLessonFilter():
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    subject_name: Optional[str] = None
    date_from: Optional[date] = None
    date_to: Optional[date] = None
