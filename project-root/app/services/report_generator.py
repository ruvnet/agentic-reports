import os
import openai
from app.utils.exa_search import search_exa
from app.core.config import settings

# Set up API keys using environment variables
openai.api_key = os.getenv('OPENAI_API_KEY', settings.openai_api_key)
exa_api_key = os.getenv('EXA_API_KEY', settings.exa_api_key)

print(f"OpenAI API Key: {openai.api_key}")
print(f"Exa API Key: {exa_api_key}")

def generate_report(topic: str) -> str:
    # Ensure API keys are set
    if not openai.api_key or not exa_api_key:
        raise ValueError("API keys are not set.")
    
    # Generate subqueries from the main topic
    subqueries = generate_subqueries_from_topic(topic)
    # Search each subquery using Exa
    exa_results = search_each_subquery_using_exa(subqueries)
    # Format Exa search results for easy consumption by the language model
    formatted_exa_results = format_exa_results_for_llm(exa_results)
    # Dynamically generate reports based on user input, including formatting and citations
    report = generate_report_from_exa_results(topic, formatted_exa_results)
    return report

def generate_subqueries_from_topic(topic: str) -> list:
    subqueries = ["subquery 1 based on " + topic, "subquery 2 based on " + topic]
    return subqueries

def search_each_subquery_using_exa(subqueries: list) -> list:
    exa_results = search_exa(subqueries, exa_api_key)
    return exa_results

def format_exa_results_for_llm(exa_results: list) -> str:
    formatted_results = "Formatted Exa results for LLM"
    for result in exa_results:
        formatted_results += "\n" + str(result)
    return formatted_results

def generate_report_from_exa_results(topic: str, formatted_exa_results: str) -> str:
    report = f"Report on {topic}: {formatted_exa_results}"
    return report
