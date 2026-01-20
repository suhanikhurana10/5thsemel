from fastapi import FastAPI
from app.upload_handler import router as upload_router

app = FastAPI(title="Braille Converter API")

app.include_router(upload_router)

@app.get("/")
def home():
    return {"status": "Braille Converter API is running"}
