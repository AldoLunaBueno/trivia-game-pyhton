import os
os.environ["DATABASE_URL"] = "postgresql://user:123@db:5432/triviadb_test"


from fastapi.testclient import TestClient # type: ignore
from main import app, db, questions
import asyncio
import pytest

client = TestClient(app)


@pytest.fixture(autouse=True)
def clear_table():
    # Cleans up test database called triviadb_test
    async def cleanup():
        await db.connect()
        await db.execute(questions.delete())
        await db.disconnect()
    asyncio.run(cleanup())

def test_create_question():
    response = client.post("/questions/", json={
        "description": "What is 2 + 2?",
        "options": ["1", "2", "3", "4"],
        "correct_answer": "4"
    })
    assert response.status_code == 201