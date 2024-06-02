from fastapi import APIRouter, HTTPException, status, Request
from app.services.report_generator import generate_report
from app.core.config import settings

router = APIRouter()

async def verify_api_key(request: Request):
    api_key = request.headers.get("x-api-key")
    if not api_key or api_key not in [settings.exa_api_key, settings.openai_api_key]:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API key")

@router.post("/generate-report")
async def generate_report_endpoint(topic: str, request: Request):
    await verify_api_key(request)
    report = generate_report(topic)
    return {"report": report}
