#!/bin/bash
export PYTHONPATH=$PYTHONPATH:/workspaces/agentic-reports/project-root
cd /workspaces/agentic-reports/project-root
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 --reload-dir /workspaces/agentic-reports/project-root
