import asyncio

from app.services.report_generator import generate_report


async def fake_generate_subqueries_from_topic(topic: str):
    return [f"{topic} adoption"]


async def fake_exa_search_each_subquery(subqueries):
    return [{"subquery": subqueries[0], "results": []}]


async def fake_generate_report_from_exa_results(topic, results):
    return f"Report for {topic}"


def test_generate_report(monkeypatch):
    monkeypatch.setattr(
        "app.services.report_generator.generate_subqueries_from_topic",
        fake_generate_subqueries_from_topic,
    )
    monkeypatch.setattr(
        "app.services.report_generator.exa_search_each_subquery",
        fake_exa_search_each_subquery,
    )
    monkeypatch.setattr(
        "app.services.report_generator.generate_report_from_exa_results",
        fake_generate_report_from_exa_results,
    )
    topic = "AI"
    report = asyncio.run(generate_report(topic))
    assert isinstance(report, str)
