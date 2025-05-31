from fastapi import FastAPI
from app.routers import example

app = FastAPI()

app.include_router(example.router)

@app.get("/")
def root():
    return {"message": "App Leyendas v1"}
