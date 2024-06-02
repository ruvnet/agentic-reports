# report_generator.py is a service module that generates a research report based on a given topic. The module uses the OpenAI API to generate subqueries and search results, and then generates a report based on the search results. The module also provides a synchronous version of the report generation function for testing purposes.
import os
import json
from datetime import datetime, timedelta
from litellm import acompletion
from app.core.config import settings

# Set up API keys using environment variables
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY', settings.openai_api_key)

async def generate_report(topic: str) -> str:
    print(f"Starting report generation for topic: {topic}")
    subqueries = await generate_subqueries_from_topic(topic)
    list_of_query_exa_pairs = exa_search_each_subquery(subqueries)
    report = await generate_report_from_exa_results(topic, list_of_query_exa_pairs)
    return report

async def generate_report_without_exa(topic):
    print(f"🚀 Generating report without Exa for topic: {topic}")
    content = f"Write a comprehensive and professional three-paragraph research report about {topic}. Include citations with source, month, and year."
    try:
        completion = await acompletion(
            model='gpt-4',
            messages=[{"role": "user", "content": content}],
            stream=False
        )
        report = completion['choices'][0]['message']['content']
    except Exception as e:
        report = f"Failed to generate report: {str(e)}"
    return report

async def generate_subqueries_from_topic(topic, num_subqueries=6):
    print(f"🌿 Generating subqueries from topic: {topic}")
    content = f"I'm going to give you a topic I want to research. I want you to generate {num_subqueries} interesting, diverse search queries that would be useful for generating a report on my main topic. Here is the main topic: {topic}."
    try:
        completion = await acompletion(
            model='gpt-4',
            messages=[{"role": "user", "content": content}],
            stream=False
        )
        json_response = json.loads(completion['choices'][0]['message']['content'])
        subqueries = list(json_response.values())
    except Exception as e:
        subqueries = [f"Failed to generate subqueries: {str(e)}"]
    return subqueries

def exa_search_each_subquery(subqueries):
    print(f"⌛ Searching each subquery")
    list_of_query_exa_pairs = []
    one_week_ago = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")

    for query in subqueries:
        try:
            # Perform the search using Exa API
            search_response = exa_client.search(
                query=query,
                startPublishedDate=one_week_ago,
                useAutoprompt=True,
                type='neural'
            )

            results = [
                {
                    "url": result["url"],
                    "text": result["text"],
                    "published_date": result["publishedDate"]
                }
                for result in search_response["results"]
            ]

            query_object = {
                'subquery': query,
                'results': results
            }
            list_of_query_exa_pairs.append(query_object)

        except Exception as e:
            print(f"⚠️ Failed to search for query '{query}': {str(e)}")
            continue

    return list_of_query_exa_pairs

def format_exa_results_for_llm(list_of_query_exa_pairs):
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
    content = (f"Write a comprehensive and professional three-paragraph research report about {topic} based on the provided information. "
               f"Include citations in the text using footnote notation ([citation #]), for example [2]. First provide the report, followed by a single `References` section "
               f"that only lists the URLs (and their published date) used, in the format [#] <url>. For the published date, only include the month and year. "
               f"Reset the citations index and ignore the order of citations in the provided information. Here is the information: {formatted_exa_content}.")
    try:
        completion = await acompletion(
            model='gpt-4',
            messages=[{"role": "user", "content": content}],
            stream=False
        )
        report = completion['choices'][0]['message']['content']
    except Exception as e:
        report = f"Failed to generate report: {str(e)}"
    return report

def generate_subqueries_from_topic_sync(topic, num_subqueries=6):
    print(f"🌿 Generating subqueries from topic: {topic}")
    content = f"I'm going to give you a topic I want to research. I want you to generate {num_subqueries} interesting, diverse search queries that would be useful for generating a report on my main topic. Here is the main topic: {topic}."
    custom_functions = create_custom_function(num_subqueries)
    completion = openai.chat.completions.create(
        model='gpt-4',
        messages=[{"role": "user", "content": content}],
        temperature=0,
        functions=custom_functions,
        function_call='auto'
    )
    json_response = json.loads(completion.choices[0].message.function_call.arguments)
    subqueries = list(json_response.values())
    return subqueries

def generate_report_sync(topic):
    print(f"Starting report generation for topic: {topic}")
    subqueries = generate_subqueries_from_topic_sync(topic)
    list_of_query_exa_pairs = exa_search_each_subquery(subqueries)
    report = generate_report_from_exa_results_sync(topic, list_of_query_exa_pairs)
    return report

def generate_report_from_exa_results_sync(topic, list_of_query_exa_pairs):
    print(f"Generating report from Exa results for topic: {topic}")
    formatted_exa_content = format_exa_results_for_llm(list_of_query_exa_pairs)
    content = (f"Write a comprehensive and professional three-paragraph research report about {topic} based on the provided information. "
               f"Include citations in the text using footnote notation ([citation #]), for example [2]. First provide the report, followed by a single `References` section "
               f"that only lists the URLs (and their published date) used, in the format [#] <url>. For the published date, only include the month and year. "
               f"Reset the citations index and ignore the order of citations in the provided information. Here is the information: {formatted_exa_content}.")
    completion = openai.chat.completions.create(
        model='gpt-4',
        messages=[{"role": "user", "content": content}]
    )
    report = completion.choices[0].message.content
    return report
