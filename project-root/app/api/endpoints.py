# endpoints.py is the place where you define the FastAPI endpoints. 
from fastapi import APIRouter, HTTPException, status, Request, Body
from app.services.report_generator import generate_report
from app.core.config import settings
from app.utils.exa_search import advanced_search_exa
from typing import Optional, List, Dict

router = APIRouter()

@router.post("/generate-report")
async def generate_report_endpoint(topic: str, request: Request):
    try:
        report = await generate_report(topic)
        return {"report": report}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.post("/advanced-search")
async def advanced_search_endpoint(
    query: str = Body(..., embed=True),
    start_published_date: Optional[str] = Body(None, embed=True),
    end_published_date: Optional[str] = Body(None, embed=True),
    include_domains: Optional[List[str]] = Body(None, embed=True),
    exclude_domains: Optional[List[str]] = Body(None, embed=True),
    highlights: Optional[Dict] = Body(None, embed=True),
    text: Optional[Dict] = Body(None, embed=True)
):
    try:
        results = advanced_search_exa(
            query=query,
            start_published_date=start_published_date,
            end_published_date=end_published_date,
            include_domains=include_domains,
            exclude_domains=exclude_domains,
            highlights=highlights,
            text=text
        )
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))