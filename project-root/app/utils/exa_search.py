# project-root/app/utils/exa_search.py

from exa_py import Exa
from app.core.config import settings
from datetime import datetime, timedelta
from typing import Optional, List, Dict

# Initialize the Exa client
exa = Exa(api_key=settings.exa_api_key)

def search_exa(subqueries: list, api_key: str, start_published_date: Optional[str] = None, end_published_date: Optional[str] = None, include_domains: Optional[List[str]] = None, exclude_domains: Optional[List[str]] = None, highlights: Optional[Dict] = None, text: Optional[Dict] = None) -> list:
    """
    Searches Exa service for each subquery using the provided API key with advanced search options.

    Args:
        subqueries (list): List of subqueries to search.
        api_key (str): API key for the Exa service.
        start_published_date (Optional[str]): Start date for published date filter.
        end_published_date (Optional[str]): End date for published date filter.
        include_domains (Optional[List[str]]): Domains to include in the search.
        exclude_domains (Optional[List[str]]): Domains to exclude from the search.
        highlights (Optional[Dict]): Configuration for highlights.
        text (Optional[Dict]): Configuration for text content retrieval.

    Returns:
        list: List of search results.

    Examples:
        - Basic search: search_exa(["query"], "api_key")
        - Search with date filters: search_exa(["query"], "api_key", start_published_date="2020-01-01", end_published_date="2020-01-31")
        - Search with domain filters: search_exa(["query"], "api_key", include_domains=["example.com"], exclude_domains=["example.net"])
        - Search with highlights and text content options: search_exa(["query"], "api_key", highlights={"num_sentences": 5}, text={"include_html_tags": True})
    """
    results = []
    one_week_ago = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")

    for subquery in subqueries:
        try:
            search_response = exa.search_and_contents(
                query=subquery,
                num_results=5,
                use_autoprompt=True,
                start_published_date=start_published_date or one_week_ago,
                end_published_date=end_published_date,
                include_domains=include_domains,
                exclude_domains=exclude_domains,
                highlights=highlights,
                text=text
            )
            results.append({'subquery': subquery, 'results': search_response.results})
        except Exception as e:
            print(f"Error making API call to Exa for '{subquery}': {e}")
            results.append({'subquery': subquery, 'error': str(e)})
    # print results for debugging subqueries
    # print(f"Search results for subqueries: {results}")
    return results

def advanced_search_exa(query: str, start_published_date: Optional[str] = None, end_published_date: Optional[str] = None, include_domains: Optional[List[str]] = None, exclude_domains: Optional[List[str]] = None, highlights: Optional[Dict] = None, text: Optional[Dict] = None) -> dict:
    """
    Performs an advanced search on Exa with customizable options.

    Args:
        query (str): The search query.
        start_published_date (Optional[str]): Start date for published date filter.
        end_published_date (Optional[str]): End date for published date filter.
        include_domains (Optional[List[str]]): Domains to include in the search.
        exclude_domains (Optional[List[str]]): Domains to exclude from the search.
        highlights (Optional[Dict]): Configuration for highlights.
        text (Optional[Dict]): Configuration for text content retrieval.

    Returns:
        dict: The search results including any specified content retrieval options.

    Examples:
        - Advanced search with all options: advanced_search_exa("query", start_published_date="2020-01-01", end_published_date="2020-01-31", include_domains=["example.com"], exclude_domains=["example.net"], highlights={"num_sentences": 5}, text={"include_html_tags": True})
    """
    try:
        search_response = exa.search_and_contents(
            query=query,
            num_results=5,
            use_autoprompt=True,
            start_published_date=start_published_date,
            end_published_date=end_published_date,
            include_domains=include_domains,
            exclude_domains=exclude_domains,
            highlights=highlights,
            text=text
        )
        return {'query': query, 'results': search_response.results}
    except Exception as e:
        print(f"Error making API call to Exa for '{query}': {e}")
        return {'query': query, 'error': str(e)}
    

def find_similar_exa(url: str, num_results: Optional[int] = 10, include_domains: Optional[List[str]] = None, exclude_domains: Optional[List[str]] = None, start_crawl_date: Optional[str] = None, end_crawl_date: Optional[str] = None, start_published_date: Optional[str] = None, end_published_date: Optional[str] = None, category: Optional[str] = None) -> dict:
    """
    Finds similar links to the provided URL using the Exa service with customizable options.

    Args:
        url (str): The URL to find similar links for.
        num_results (Optional[int]): Number of search results to return.
        include_domains (Optional[List[str]]): Domains to include in the search.
        exclude_domains (Optional[List[str]]): Domains to exclude from the search.
        start_crawl_date (Optional[str]): Start date for crawl date filter.
        end_crawl_date (Optional[str]): End date for crawl date filter.
        start_published_date (Optional[str]): Start date for published date filter.
        end_published_date (Optional[str]): End date for published date filter.
        category (Optional[str]): Category to focus on.
        contents (Optional[Dict]): Configuration for contents retrieval.

    Returns:
        dict: The search results including any specified content retrieval options.
    """
    try:
        search_response = exa.find_similar(
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
        return {'url': url, 'results': search_response.results}
    except Exception as e:
        print(f"Error making API call to Exa for '{url}': {e}")
        return {'url': url, 'error': str(e)}