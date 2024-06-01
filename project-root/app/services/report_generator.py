import openai
from app.utils.exa_search import search_exa

def generate_report(topic: str) -> str:
    subqueries = generate_subqueries(topic)
    exa_results = search_exa(subqueries)
    report = create_report_from_exa_results(topic, exa_results)
    return report

def generate_subqueries(topic: str) -> list:
    # Generate subqueries based on the topic
    pass

def create_report_from_exa_results(topic: str, exa_results: list) -> str:
    # Create a report based on Exa search results
    pass
