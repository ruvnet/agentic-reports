## Agentic Reports

# Comprehensive System Implementation with FastAPI, Pydantic, Pandas, Exa, and Pytest

Welcome to the comprehensive system implementation guide. This document will walk you through setting up and implementing a system using FastAPI, Pydantic, Pandas, Exa, and Pytest. We will also cover the creation of a bash installation script, .devcontainer configuration, requirements.txt, folder and file structure, and necessary modules.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Prerequisites](#prerequisites)
3. [Folder and File Structure](#folder-and-file-structure)
4. [Installation](#installation)
5. [Configuration](#configuration)
6. [Modules and Functions](#modules-and-functions)
7. [Testing](#testing)
8. [Running the Application](#running-the-application)
9. [References](#references)

## Project Overview

This project aims to create a high-performance API using FastAPI, Pydantic for data validation, Pandas for data manipulation, Exa for search capabilities, and Pytest for testing. The system will generate comprehensive research reports based on user queries.

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- Python 3.7+
- Docker
- Git

## Folder and File Structure

The project structure is organized as follows:

```
project-root/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── endpoints.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── report.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── report_generator.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── exa_search.py
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   ├── test_report_generator.py
├── .devcontainer/
│   ├── devcontainer.json
│   ├── Dockerfile
├── requirements.txt
├── install.sh
├── README.md
```

## Installation

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd project-root
```

### Step 2: Run the Installation Script

```bash
chmod +x install.sh
./install.sh
```

### Step 3: Set Up the Development Container

Ensure you have Docker installed and running. Open the project in Visual Studio Code and use the Remote - Containers extension to open the project in a container.

## Configuration

### .devcontainer/devcontainer.json

```json
{
    "name": "FastAPI Project",
    "dockerFile": "Dockerfile",
    "settings": {
        "terminal.integrated.shell.linux": "/bin/bash"
    },
    "extensions": [
        "ms-python.python",
        "ms-azuretools.vscode-docker"
    ],
    "postCreateCommand": "pip install -r requirements.txt"
}
```

### .devcontainer/Dockerfile

```Dockerfile
FROM python:3.9-slim

WORKDIR /workspace

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
```

### requirements.txt

```txt
fastapi
pydantic
pandas
exa_py
pytest
uvicorn
```

## Modules and Functions

### app/main.py

```python
from fastapi import FastAPI
from app.api import endpoints

app = FastAPI()

app.include_router(endpoints.router)
```

### app/api/endpoints.py

```python
from fastapi import APIRouter
from app.services.report_generator import generate_report

router = APIRouter()

@router.post("/generate-report")
async def generate_report_endpoint(topic: str):
    report = generate_report(topic)
    return {"report": report}
```

### app/core/config.py

```python
from pydantic import BaseSettings

class Settings(BaseSettings):
    exa_api_key: str
    openai_api_key: str

settings = Settings()
```

### app/models/report.py

```python
from pydantic import BaseModel

class Report(BaseModel):
    topic: str
    content: str
```

### app/services/report_generator.py

```python
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
```

### app/utils/exa_search.py

```python
from exa_py import Exa
from app.core.config import settings

exa = Exa(api_key=settings.exa_api_key)

def search_exa(subqueries: list) -> list:
    results = []
    for query in subqueries:
        response = exa.search(query)
        results.append(response)
    return results
```

## Testing

### tests/test_main.py

```python
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_generate_report():
    response = client.post("/generate-report", json={"topic": "AI"})
    assert response.status_code == 200
    assert "report" in response.json()
```

### tests/test_report_generator.py

```python
from app.services.report_generator import generate_report

def test_generate_report():
    topic = "AI"
    report = generate_report(topic)
    assert isinstance(report, str)
```

## Running the Application

To run the application, use the following command:

```bash
uvicorn app.main:app --reload
```

## References

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)
- [Pandas Documentation](https://pandas.pydata.org/)
- [Exa Documentation](https://exa.ai/)
- [Pytest Documentation](https://docs.pytest.org/)

This detailed plan should help you set up and implement the system effectively. If you have any questions or need further assistance, feel free to reach out.

Citations:
[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/2592765/73f4bc8c-837f-4711-a4b5-d4dadd91f486/paste.txt
[2] https://fastapi.tiangolo.com/tutorial/testing/
[3] https://www.youtube.com/watch?v=qNVsQ4R9Lsg
[4] https://shuaib.org/python/fastapi/quickly-set-up-a-fastapi-app-with-this-script/
[5] https://www.youtube.com/watch?v=jM-zWp8dNQA
[6] https://dev.to/timo_reusch/how-i-structure-big-fastapi-projects-260e
[7] https://www.reddit.com/r/FastAPI/comments/uxnso3/fastapi_large_app_structure/
[8] https://stackoverflow.com/questions/70448668/passing-pandas-dataframe-to-fastapi
[9] https://testdriven.io/blog/fastapi-crud/
[10] https://andypickup.com/developing-in-python-with-dev-containers-part-2-a-simple-fastapi-project-with-step-debugging-e52599b7ce61?gi=beae3ea2f4fd
[11] https://fastapi.tiangolo.com/features/
[12] https://fastapi.tiangolo.com/tutorial/first-steps/
[13] https://github.com/rochacbruno/fastapi-project-template/blob/main/requirements.txt
[14] https://fastapi.tiangolo.com/advanced/settings/
[15] https://plainenglish.io/blog/how-to-generate-requirements-txt-for-your-python-project-235183799d2f
[16] https://pytest-with-eric.com/pytest-advanced/pytest-fastapi-testing/
[17] https://christophergs.com/tutorials/ultimate-fastapi-tutorial-pt-4-pydantic-schemas/
[18] https://fastapi.tiangolo.com/tutorial/schema-extra-example/
[19] https://www.reddit.com/r/FastAPI/comments/115en24/help_how_to_make_ml_predictions_of_a_pandas/
[20] https://fastapi.tiangolo.com/deployment/docker/
