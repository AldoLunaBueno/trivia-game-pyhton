from fastapi import FastAPI # type: ignore
import databases # type: ignore
import os
from pydantic import BaseModel # type: ignore
import sqlalchemy  # type: ignore
from typing import List

DATABASE_URL = os.getenv("DATABASE_URL",  "postgresql://user:123@db:5432/triviadb")
db = databases.Database(DATABASE_URL)

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

questions = sqlalchemy.Table(
    "questions",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("description", sqlalchemy.String),
    sqlalchemy.Column("options", sqlalchemy.ARRAY(sqlalchemy.String)),
    sqlalchemy.Column("correct_answer", sqlalchemy.String),
    sqlalchemy.Column("difficulty", sqlalchemy.Integer)
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await db.connect()
    print("Conected to postgresql")

@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()
    print("Disconnected from postgresql")

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI!"}

class QuestionCreate(BaseModel):
    description: str
    options: List[str]
    correct_answer: int
    difficulty: int
    
@app.get("/questions/", status_code=201)
async def create_questions(question: QuestionCreate):
    query = questions.insert().values(
        description = question.description,
        options = question.options,
        correct_answer = question.correct_answer,
        difficulty = questions.difficulty
    )
    await db.execute(query)
    return {"message": "Question created"}