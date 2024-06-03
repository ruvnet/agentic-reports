import os
import subprocess
import sys
import importlib.util

def check_and_install_python3_10():
    try:
        # Check if Python 3.10 is installed
        subprocess.run(['python3.10', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except (subprocess.CalledProcessError, FileNotFoundError):
        # Python 3.10 is not installed, attempt to install it
        print("❗ Python 3.10 is not installed. Attempting to install Python 3.10...")
        try:
            if sys.platform.startswith('linux'):
                subprocess.run(['sudo', 'apt-get', 'update'], check=True)
                subprocess.run(['sudo', 'apt-get', 'install', '-y', 'python3.10', 'python3.10-venv', 'python3.10-dev'], check=True)
                print("✅ Python 3.10 installed successfully.")
            else:
                print("❗ Automatic installation is not supported on this OS. Please install Python 3.10 manually.")
                sys.exit(1)
        except Exception as e:
            print(f"❗ Failed to install Python 3.10: {e}")
            sys.exit(1)

def check_and_install_requirements(python_executable):
    print("📦 Installing required packages...")
    required_packages = ['fastapi', 'pydantic', 'pandas', 'exa_py', 'pytest', 'uvicorn', 'pydantic-settings', 'litellm']
    subprocess.run([python_executable, '-m', 'pip', 'install'] + required_packages, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print("✅ Packages installed.")

def prompt_for_api_key(env_var_name):
    api_key = input(f"🔑 Enter your {env_var_name}: ")
    os.environ[env_var_name] = api_key
    subprocess.run(['export', f'{env_var_name}={api_key}'], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"✅ {env_var_name} set.")

def main():
    print(r"""
 _____             _   _         _____                 _       
|  _  |___ ___ ___| |_|_|___ ___| __  |___ ___ ___ ___| |_ ___ 
|     | . | -_|   |  _| |  _|___|    -| -_| . | . |  _|  _|_ -|
|__|__|_  |___|_|_|_| |_|___|   |__|__|___|  _|___|_| |_| |___|
      |___|                               |_|                  

A Comprehensive Python Library for Generating Research Reports
    """)

    print("🚀 Starting the Agentic Reports application setup and server...")

    # Check for Python 3.10 installation
    check_and_install_python3_10()

    # Check for OPENAI_API_KEY
    if not os.getenv('OPENAI_API_KEY'):
        prompt_for_api_key('OPENAI_API_KEY')

    # Check for EXA_API_KEY
    if not os.getenv('EXA_API_KEY'):
        prompt_for_api_key('EXA_API_KEY')

    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"📂 Script directory: {script_dir}")

    # Set PYTHONPATH to include the project root directory
    os.environ['PYTHONPATH'] = os.environ.get('PYTHONPATH', '') + f':{script_dir}'
    print("✅ PYTHONPATH set.")

    # Ensure the correct working directory
    os.chdir(script_dir)
    print("✅ Working directory set.")

    # Create a virtual environment using Python 3.10 if it doesn't exist
    venv_dir = os.path.join(script_dir, 'venv')
    if not os.path.exists(venv_dir):
        print("🐍 Creating virtual environment with Python 3.10...")
        subprocess.run(['python3.10', '-m', 'venv', 'venv'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("✅ Virtual environment created.")

    # Use the Python executable from the virtual environment
    venv_python = os.path.join(venv_dir, 'bin', 'python')
    if sys.platform == 'win32':
        venv_python = os.path.join(venv_dir, 'Scripts', 'python')
    print(f"🐍 Using Python executable: {venv_python}")

    # Check and install required packages
    check_and_install_requirements(venv_python)

    # Run Uvicorn with the necessary parameters and show its output
    print("🌐 Starting Uvicorn server...")
    subprocess.run([venv_python, '-m', 'uvicorn', 'app.main:app', '--reload', '--host', '0.0.0.0', '--port', '8000', '--reload-dir', script_dir])
    print("🚀 Uvicorn server started.")

if __name__ == "__main__":
    main()
