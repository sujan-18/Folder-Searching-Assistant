from fastapi import FastAPI
from app.routers import files

app = FastAPI()
app.include_router(files.router)


@app.get("/")
def root():
    return{"message":"My Assistant API is running"}
    