from fastapi import APIRouter, HTTPException, status, Body
from typing import List, Optional, Dict
from app.services.report_generator import generate_advanced_report

router = APIRouter()

@router.post("/generate-report-advanced")
async def generate_report_advanced_endpoint(
    query: str = Body(..., example="quantum computing"),
    primary_prompt: str = Body(..., example="Generate a detailed report on the current advancements and applications of quantum computing."),
    subqueries_prompt: str = Body(..., example="Please create subqueries related to quantum computing advancements and its various applications."),
    report_prompt: str = Body(..., example="Write a comprehensive and professional in french, five-paragraph, 800 word research report about quantum computing based on the provided information."),
    start_published_date: Optional[str] = Body(None, example="2023-01-01"),
    end_published_date: Optional[str] = Body(None, example="2023-12-31"),
    include_domains: Optional[List[str]] = Body(None, example=["example.com", "another-example.com"]),
    exclude_domains: Optional[List[str]] = Body(None, example=["excluded.com"]),
    highlights: Optional[Dict] = Body(None, example={"num_sentences": 5}),
    text: Optional[Dict] = Body(None, example={"include_html_tags": False}),
    num_subqueries: int = Body(10, example=10)
):
    try:
        report = await generate_advanced_report(
            query=query,
            primary_prompt=primary_prompt,
            subqueries_prompt=subqueries_prompt,
            report_prompt=report_prompt,
            start_published_date=start_published_date,
            end_published_date=end_published_date,
            include_domains=include_domains,
            exclude_domains=exclude_domains,
            highlights=highlights,
            text=text,
            num_subqueries=num_subqueries
        )
        return {"report": report}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
