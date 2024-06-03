#!/bin/bash

echo "                                                              
 _____             _   _         _____                 _       
|  _  |___ ___ ___| |_|_|___ ___| __  |___ ___ ___ ___| |_ ___ 
|     | . | -_|   |  _| |  _|___|    -| -_| . | . |  _|  _|_ -|
|__|__|_  |___|_|_|_| |_|___|   |__|__|___|  _|___|_| |_| |___|
      |___|                               |_|                  

A Comprehensive Python Library for Generating Research Reports
"

# Starting message
echo "Starting the Agentic Reports application setup and server..."

# Check for OPENAI_API_KEY
if [ -z "$OPENAI_API_KEY" ]; then
    read -p "Enter your OPENAI_API_KEY: " openai_key
    export OPENAI_API_KEY=$openai_key
fi

# Check for EXA_API_KEY
if [ -z "$EXA_API_KEY" ]; then
    read -p "Enter your EXA_API_KEY: " exa_key
    export EXA_API_KEY=$exa_key
fi

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
