from exa_py import Exa
from app.core.config import settings

exa = Exa(api_key=settings.exa_api_key)

def search_exa(subqueries: list) -> list:
    results = []
    for query in subqueries:
        response = exa.search(query)
        results.append(response)
    return results
