# project-root/app/utils/exa_search.py
from exa_py import Exa
from app.core.config import settings
import requests

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
    for subquery in subqueries:
        result = api_call_to_exa(subquery, api_key)
        results.append(result)
    return results

def api_call_to_exa(subquery: str, api_key: str) -> dict:
    """
    Makes an API call to the Exa service.

    Args:
        subquery (str): The subquery to search.
        api_key (str): API key for the Exa service.

    Returns:
        dict: The response from the Exa service.
    """
    url = f"https://api.exa.com/v1/search?q={subquery}"
    headers = {"Authorization": f"Bearer {api_key}"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error making API call to Exa: {e}")
        return {}