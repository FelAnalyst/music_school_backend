import logging
from fastapi import FastAPI

logging.basicConfig(level=logging.INFO)

app = FastAPI()

@app.on_event("startup")
def startup():
    logging.info("Application started")

@app.get("/")
def home():
    return {"status": "ok", "message": "Music School backend running"}
