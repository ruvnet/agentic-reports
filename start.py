# start.py

import os
import subprocess
import sys

def main():
    print("Starting the Agentic Reports application setup and server...")

    # Set PYTHONPATH to include the project root directory
    os.environ['PYTHONPATH'] = os.environ.get('PYTHONPATH', '') + ':/workspaces/agentic-reports/project-root'

    # Ensure the correct working directory
    os.chdir('/workspaces/agentic-reports/project-root')

    # Create a virtual environment if it doesn't exist
    if not os.path.exists('venv'):
        subprocess.run([sys.executable, '-m', 'venv', 'venv'])

    # Activate the virtual environment
    activate_script = './venv/bin/activate'
    if sys.platform == 'win32':
        activate_script = '.\\venv\\Scripts\\activate'
    
    # Install required dependencies quietly
    subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', '../requirements.txt', '-q'])

    # Modify the PATH to include the virtual environment's bin directory
    os.environ['PATH'] = os.path.abspath('venv/bin') + os.pathsep + os.environ.get('PATH', '')

    # Run Uvicorn with the necessary parameters
    subprocess.run(['uvicorn', 'app.main:app', '--reload', '--host', '0.0.0.0', '--port', '8000', '--reload-dir', '/workspaces/agentic-reports/project-root'])

if __name__ == "__main__":
    main()
