from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_question():
    response = client.post("/questions/", json={
        "description": "What is 2 + 2?",
        "options": ["1", "2", "3", "4"],
        "correct_answer": "4"
    })
    assert response.status_code == 201