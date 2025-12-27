import logging
from fastapi import FastAPI, Depends
from app.services.students.schemas import StudentFilter
from app.services.students.service import get_students

logging.basicConfig(level=logging.INFO)

app = FastAPI()

@app.on_event("startup")
def startup():
    logging.info("Application started")

@app.get("/")
def home():
    return {"status": "ok", "message": "Music School backend running"}

@app.get("/students")
def students(filters: StudentFilter = Depends()):
    return get_students(filters)
