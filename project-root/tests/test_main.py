from fastapi.testclient import TestClient
from app.api import endpoints
from app.main import app

client = TestClient(app)


async def fake_generate_report(topic: str, company_domain: str | None = None) -> str:
    return f"Report for {topic}"


def test_generate_report(monkeypatch):
    monkeypatch.setattr(endpoints, "generate_report", fake_generate_report)
    response = client.post("/generate-report", json={"topic": "AI"})
    assert response.status_code == 200
    assert "report" in response.json()
