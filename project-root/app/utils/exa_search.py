# project-root/app/utils/exa_search.py


from exa_py import Exa
from app.core.config import settings
from datetime import datetime, timedelta

# Initialize the Exa client
exa = Exa(api_key=settings.exa_api_key)

def search_exa(subqueries: list, api_key: str) -> list:
    """
    Searches Exa service for each subquery using the provided API key.

    Args:
        subqueries (list): List of subqueries to search.
        api_key (str): API key for the Exa service.

    Returns:
        list: List of search results.
    """
    results = []
    one_week_ago = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")

    for subquery in subqueries:
        try:
            search_response = exa.search_and_contents(
                query=subquery,
                num_results=5,
                use_autoprompt=True,
                # start_published_date=one_week_ago,
                highlights={"num_sentences": 5},
            )
            results.append({'subquery': subquery, 'results': search_response.results})
        except Exception as e:
            print(f"Error making API call to Exa for '{subquery}': {e}")
            results.append({'subquery': subquery, 'error': str(e)})
    print(f"Search results for subqueries: {results}")
    return results
