from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_generate_report():
    response = client.post("/generate-report", json={"topic": "AI"})
    assert response.status_code == 200
    assert "report" in response.json()
