from fastapi import FastAPI # type: ignore
import databases # type: ignore
from contextlib import asynccontextmanager
import os
from pydantic import BaseModel # type: ignore
import sqlalchemy  # type: ignore
from typing import List

DATABASE_URL = os.getenv("DATABASE_URL",  "postgresql://user:123@db:5432/triviadb")
db = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

questions = sqlalchemy.Table(
    "questions",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("description", sqlalchemy.String),
    sqlalchemy.Column("options", sqlalchemy.ARRAY(sqlalchemy.String)),
    sqlalchemy.Column("correct_answer", sqlalchemy.Integer),
    sqlalchemy.Column("difficulty", sqlalchemy.Integer)
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.drop_all(engine)
metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.connect()
    print("Connected to PostgreSQL")
    yield
    await db.disconnect()
    print("Disconnected from PostgreSQL")

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI!"}

class QuestionCreate(BaseModel):
    description: str
    options: List[str]
    correct_answer: int
    difficulty: int
    
@app.post("/questions/", status_code=201)
async def create_questions(question: QuestionCreate):
    if not db.is_connected:
        await db.connect()
        
    query = questions.insert().values(
        description = question.description,
        options = question.options,
        correct_answer = question.correct_answer,
        difficulty = question.difficulty
    )
    await db.execute(query)
    return {"message": "Question created"}