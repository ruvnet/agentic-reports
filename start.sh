#!/bin/bash

# Starting message
echo "Starting the Agentic Reports application setup and server..."

# Set PYTHONPATH to include the project root directory
export PYTHONPATH=$PYTHONPATH:/workspaces/agentic-reports/project-root

# Ensure the correct working directory
cd /workspaces/agentic-reports/project-root

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install required dependencies quietly
pip install -r ../requirements.txt -q

# Run Uvicorn with the necessary parameters
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 --reload-dir /workspaces/agentic-reports/project-root
