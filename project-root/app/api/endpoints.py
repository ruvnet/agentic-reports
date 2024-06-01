from fastapi import APIRouter
from app.services.report_generator import generate_report

router = APIRouter()

@router.post("/generate-report")
async def generate_report_endpoint(topic: str):
    report = generate_report(topic)
    return {"report": report}
