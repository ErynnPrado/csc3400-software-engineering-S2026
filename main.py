from fastapi import FastAPI
from database import init_database
from routes import router

app = FastAPI(title="Student Management API")
app.include_router(router)

@app.on_event("startup")
def startup():
    init_database()
    print("Database initialized!")

@app.get("/")
def root():
    return {"message": "Student Management API", "docs": "/docs"}
