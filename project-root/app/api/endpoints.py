# endpoints.py is the place where you define the FastAPI endpoints. 

from fastapi import APIRouter, HTTPException, status, Request, Body
from app.services.report_generator import generate_report, generate_subqueries_from_topic, exa_search_each_subquery
from app.core.config import settings
from app.utils.exa_search import advanced_search_exa, find_similar_exa
from typing import Optional, List, Dict
from .advanced_reports import router as advanced_reports_router

router = APIRouter()

@router.post("/generate-report")
async def generate_report_endpoint(topic: str, request: Request):
    try:
        report = await generate_report(topic)
        return {"report": report}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.post("/generate-subqueries")
async def generate_subqueries_endpoint(
    topic: str = Body(..., embed=True, example="Latest AI jobs in Toronto"),
    num_subqueries: int = Body(10, embed=True, example=10)
):
    try:
        subqueries = await generate_subqueries_from_topic(topic, num_subqueries)
        return {"subqueries": subqueries}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.post("/search-subqueries")
async def search_subqueries_endpoint(
    subqueries: List[str] = Body(..., embed=True, example=["AI job market in Canada", "Top AI companies hiring in Toronto"])
):
    try:
        list_of_query_exa_pairs = await exa_search_each_subquery(subqueries)
        return {"results": list_of_query_exa_pairs}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.post("/advanced-search")
async def advanced_search_endpoint(
    query: str = Body("New York City condos", embed=True),
    start_published_date: Optional[str] = Body("2023-01-01", embed=True),
    end_published_date: Optional[str] = Body("2023-12-31", embed=True),
    include_domains: Optional[List[str]] = Body(None, embed=True),
    exclude_domains: Optional[List[str]] = Body(None, embed=True),
    highlights: Optional[Dict] = Body({"num_sentences": 3}, embed=True),
    text: Optional[Dict] = Body({"include_html_tags": False}, embed=True)
):
    try:
        # Ensure only one of include_domains or exclude_domains is specified
        if include_domains and exclude_domains:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Only one of include_domains or exclude_domains can be specified."
            )

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
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.post("/find-similar-links", summary="Find similar links to the provided URL")
async def find_similar_links_endpoint(
    url: str = Body(..., embed=True, example="https://drudgereport.com"),
    num_results: Optional[int] = Body(10, embed=True, example=10),
    include_domains: Optional[List[str]] = Body(None, embed=True, example=["example.com"]),
    exclude_domains: Optional[List[str]] = Body(None, embed=True, example=["excluded.com"]),
    start_crawl_date: Optional[str] = Body(None, embed=True, example="2023-01-01"),
    end_crawl_date: Optional[str] = Body(None, embed=True, example="2023-12-31"),
    start_published_date: Optional[str] = Body(None, embed=True, example="2023-01-01"),
    end_published_date: Optional[str] = Body(None, embed=True, example="2023-12-31"),
    category: Optional[str] = Body(None, embed=True, example="news")
):
    try:
        # Ensure only one of include_domains or exclude_domains is specified
        if include_domains and exclude_domains:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Only one of include_domains or exclude_domains can be specified."
            )

        results = find_similar_exa(
            url=url,
            num_results=num_results,
            include_domains=include_domains,
            exclude_domains=exclude_domains,
            start_crawl_date=start_crawl_date,
            end_crawl_date=end_crawl_date,
            start_published_date=start_published_date,
            end_published_date=end_published_date,
            category=category
        )
        return {"results": results}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)) 

# Include the advanced_reports router
router.include_router(advanced_reports_router, prefix="/api/v1", tags=["advanced-reports"])