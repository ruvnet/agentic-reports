# endpoints.py is the place where you define the FastAPI endpoints. 
from fastapi import APIRouter, HTTPException, status, Request
from app.services.report_generator import generate_report
from app.core.config import settings

router = APIRouter()

@router.post("/generate-report")
async def generate_report_endpoint(topic: str, request: Request):
    try:
        report = await generate_report(topic)
        return {"report": report}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
