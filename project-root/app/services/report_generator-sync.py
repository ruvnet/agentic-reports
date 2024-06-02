# project-root/app/services/report_generator-sync.py is a synchronous version of the report_generator.py service. 
# It uses the synchronous version of the OpenAI API client and synchronous Exa search functions. 
# This version is suitable for applications that require synchronous processing or do not support asynchronous operations. 
# The functions in this module perform the following tasks: 
# - Initialize the Exa client for searching the Exa service.
# - Generate subqueries from a given topic using the GPT-4 model.
# - Search Exa for each subquery to retrieve relevant information.
# - Format the Exa search results for input to the GPT-4 model.
# - Generate a research report based on the Exa search results using the GPT-4 model.
# - Perform a search with retries and exponential backoff.
# - Provide a synchronous version of the report generation process.

import os
import json
import time

import asyncio
import aiohttp

from datetime import datetime, timedelta
from litellm import acompletion
from app.core.config import settings
from app.utils.exa_search import search_exa

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
            model='gpt-4o',
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
            model='gpt-4o',
            messages=[{"role": "user", "content": content}],
            stream=False
        )
        response_content = completion['choices'][0]['message']['content']
        print(f"Raw response content: {response_content}")  # Print raw response for debugging
        
        # Split the response into individual lines and strip leading/trailing spaces and numbers
        subqueries = []
        for line in response_content.split('\n'):
            if line.strip():
                # Attempt to split by ". " and take the second part
                try:
                    subquery = line.strip(' "').split('. ', 1)[1]
                    subqueries.append(subquery)
                except IndexError:
                    print(f"Skipping improperly formatted line: {line}")
        
        # Output the parsed subqueries for debugging
        print(f"Parsed subqueries: {subqueries}")
        
    except Exception as e:
        print(f"Unexpected error: {str(e)}")  # Output unexpected error details
        subqueries = [f"Failed to generate subqueries: {str(e)}"]
    return subqueries

def exa_search_each_subquery(subqueries):
    print(f"⌛ Searching each subquery")
    list_of_query_exa_pairs = []

    # Initialize the Exa client (assuming you have the initialization code)
    exa_client = initialize_exa_client()  # Add your initialization logic here

    if exa_client is None:
        print("⚠️ Exa client is not initialized. Check your initialization logic.")
        return []

    def perform_search(query, retries=5, delay=2):
        """Helper function to perform search with retries and exponential backoff."""
        for attempt in range(retries):
            try:
                # Perform the search using Exa API
                search_response = exa_client.search_and_contents(
                    query=query,
                    type='neural'
                )
                # Check if response contains data
                if search_response and hasattr(search_response, 'results') and search_response.results:
                    return search_response
                else:
                    print(f"⚠️ No data found for subquery: {query}")
                    return None
            except Exception as e:
                print(f"⚠️ Attempt {attempt + 1} failed for query '{query}': {str(e)}")
                if "502" in str(e) and attempt < retries - 1:
                    backoff = delay * (2 ** attempt)  # Exponential backoff
                    print(f"Retrying in {backoff} seconds...")
                    time.sleep(backoff)
                else:
                    print(f"⚠️ All {retries} attempts failed for query '{query}'")
                    return None

    for query in subqueries:
        if "Failed to generate subqueries" in query:
            print(f"⚠️ Skipping invalid subquery: {query}")
            continue

        print(f"🔍 Searching for subquery: {query}")
        search_response = perform_search(query)
        if search_response:
            print(f"✅ Search successful for subquery: {query}")
            list_of_query_exa_pairs.append({
                'subquery': query,
                'results': search_response.results
            })

    print(f"🏁 Completed search for all subqueries")
    return list_of_query_exa_pairs

def format_exa_results_for_llm(list_of_query_exa_pairs):
    print(f"⌨️  Formatting Exa results for LLM")
    formatted_string = ""
    for pair in list_of_query_exa_pairs:
        formatted_string += f"[{pair['subquery']}]:\n"
        for result in pair['results']:
            content = getattr(result, 'text', "No text available")
            publish_date = getattr(result, 'published_date', "No date available")
            url = getattr(result, 'url', "No URL available")
            formatted_string += f"URL: {url}\nContent: {content}\nPublish Date: {publish_date}\n"
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
            model='gpt-4o',
            messages=[{"role": "user", "content": content}],
            stream=False
        )
        report = completion['choices'][0]['message']['content']
    except Exception as e:
        report = f"Failed to generate report: {str(e)}"
    return report

def initialize_exa_client():
    from exa_py import Exa
    try:
        exa_client = Exa(api_key=settings.exa_api_key)
        return exa_client
    except Exception as e:
        print(f"⚠️ Failed to initialize Exa client: {str(e)}")
        return None

# For synchronous version if needed
def generate_subqueries_from_topic_sync(topic, num_subqueries=6):
    print(f"🌿 Generating subqueries from topic: {topic}")
    content = f"I'm going to give you a topic I want to research. I want you to generate {num_subqueries} interesting, diverse search queries that would be useful for generating a report on my main topic. Here is the main topic: {topic}."
    try:
        completion = openai.ChatCompletion.create(
            model='gpt-4o',
            messages=[{"role": "user", "content": content}]
        )
        response_content = completion['choices'][0]['message']['content']
        print(f"Raw response content: {response_content}")  # Print raw response for debugging
        
        # Split the response into individual lines and strip leading/trailing spaces and numbers
        subqueries = []
        for line in response_content.split('\n'):
            if line.strip():
                # Attempt to split by ". " and take the second part
                try:
                    subquery = line.strip(' "').split('. ', 1)[1]
                    subqueries.append(subquery)
                except IndexError:
                    print(f"Skipping improperly formatted line: {line}")
        
        # Output the parsed subqueries for debugging
        print(f"Parsed subqueries: {subqueries}")
        
    except Exception as e:
        print(f"Unexpected error: {str(e)}")  # Output unexpected error details
        subqueries = [f"Failed to generate subqueries: {str(e)}"]
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
    completion = openai.ChatCompletion.create(
        model='gpt-4o',
        messages=[{"role": "user", "content": content}]
    )
    report = completion.choices[0].message.content
    return report
