import os
import subprocess
import sys

def prompt_for_api_key(env_var_name):
    api_key = input(f"Enter your {env_var_name}: ")
    os.environ[env_var_name] = api_key
    subprocess.run(['export', f'{env_var_name}={api_key}'], shell=True)

def main():
    print(r"""
 _____             _   _         _____                 _       
|  _  |___ ___ ___| |_|_|___ ___| __  |___ ___ ___ ___| |_ ___ 
|     | . | -_|   |  _| |  _|___|    -| -_| . | . |  _|  _|_ -|
|__|__|_  |___|_|_|_| |_|___|   |__|__|___|  _|___|_| |_| |___|
      |___|                               |_|                  

A Comprehensive Python Library for Generating Research Reports
    """)

    print("Starting the Agentic Reports application setup and server...")

    # Check for OPENAI_API_KEY
    if not os.getenv('OPENAI_API_KEY'):
        prompt_for_api_key('OPENAI_API_KEY')

    # Check for EXA_API_KEY
    if not os.getenv('EXA_API_KEY'):
        prompt_for_api_key('EXA_API_KEY')

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
