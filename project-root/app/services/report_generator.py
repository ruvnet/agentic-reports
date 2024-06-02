import os
import json
import openai
from datetime import datetime, timedelta
from app.core.config import settings

# Set up API keys using environment variables
openai.api_key = os.getenv('OPENAI_API_KEY', settings.openai_api_key)

async def generate_report(topic: str) -> str:
    print(f"Starting report generation for topic: {topic}")
    subqueries = await generate_subqueries_from_topic(topic)
    list_of_query_exa_pairs = exa_search_each_subquery(subqueries)
    report = await generate_report_from_exa_results(topic, list_of_query_exa_pairs)
    return report

async def generate_report_without_exa(topic):
    print(f"🚀 Generating report without Exa for topic: {topic}")
    print(f"")
    content = f"Write a comprehensive and professional three paragraph research report about {topic}. Include citations with source, month, and year."
    completion = await openai.chat.completions.create(
        model='gpt-4',
        messages=[{"role": "user", "content": content}],
        temperature=0
    )
    report = completion.choices[0].message['content']
    return report

def create_custom_function(num_subqueries):
    properties = {}
    for i in range(1, num_subqueries + 1):
        key = f'subquery_{i}'
        properties[key] = {
            'type': 'string',
            'description': 'Search queries that would be useful for generating a report on my main topic'
        }

    custom_function = {
        'name': 'generate_exa_search_queries',
        'description': 'Generates Exa search queries to investigate the main topic',
        'parameters': {
            'type': 'object',
            'properties': properties
        }
    }

    return [custom_function]

async def generate_subqueries_from_topic(topic, num_subqueries=6):
    print(f" ")
    print(f"🌿 Generating subqueries from topic: {topic}")
    content = f"I'm going to give you a topic I want to research. I want you to generate {num_subqueries} interesting, diverse search queries that would be useful for generating a report on my main topic. Here is the main topic: {topic}."
    custom_functions = create_custom_function(num_subqueries)
    completion = await openai.chat.completions.create(
        model='gpt-4',
        messages=[{"role": "user", "content": content}],
        temperature=0,
        functions=custom_functions,
        function_call='auto'
    )
    json_response = json.loads(completion.choices[0].message['function_call']['arguments'])
    subqueries = list(json_response.values())
    return subqueries

def exa_search_each_subquery(subqueries):
    print(f"")
    print(f"⌛ Searching each subquery")
    list_of_query_exa_pairs = []
    one_week_ago = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
    for query in subqueries:
        search_response = {
            "results": [
                {
                    "url": "http://example.com",
                    "text": "Example text",
                    "published_date": one_week_ago
                }
            ]
        }
        query_object = {
            'subquery': query,
            'results': search_response['results']
        }
        list_of_query_exa_pairs.append(query_object)
    return list_of_query_exa_pairs

def format_exa_results_for_llm(list_of_query_exa_pairs):
    print(f"")
    print(f"⌨️  Formatting Exa results for LLM")
    formatted_string = ""
    for i in list_of_query_exa_pairs:
        formatted_string += f"[{i['subquery']}]:\n"
        for result in i['results']:
            content = result.get('text', "No text available")
            publish_date = result.get('published_date', "No date available")
            formatted_string += f"URL: {result['url']}\nContent: {content}\nPublish Date: {publish_date}\n"
        formatted_string += "\n"
    return formatted_string

async def generate_report_from_exa_results(topic, list_of_query_exa_pairs):
    print(f"Generating report from Exa results for topic: {topic}")
    formatted_exa_content = format_exa_results_for_llm(list_of_query_exa_pairs)
    content = (f"Write a comprehensive and professional three paragraph research report about {topic} based on the provided information. "
               f"Include citations in the text using footnote notation ([citation #]), for example [2]. First provide the report, followed by a single `References` section "
               f"that only lists the URLs (and their published date) used, in the format [#] <url>. For the published date, only include the month and year. "
               f"Reset the citations index and ignore the order of citations in the provided information. Here is the information: {formatted_exa_content}.")
    completion = await openai.chat.completions.create(
        model='gpt-4',
        messages=[{"role": "user", "content": content}]
    )
    report = completion.choices[0].message['content']
    return report
