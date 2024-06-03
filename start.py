import os
import subprocess

def prompt_for_api_key(env_var_name):
    api_key = input(f"Enter your {env_var_name}: ")
    os.environ[env_var_name] = api_key

def main():
    # Check for OPENAI_API_KEY
    if not os.getenv('OPENAI_API_KEY'):
        prompt_for_api_key('OPENAI_API_KEY')

    # Check for EXA_API_KEY
    if not os.getenv('EXA_API_KEY'):
        prompt_for_api_key('EXA_API_KEY')

    # Run the shell script
    subprocess.run(['bash', './start.sh'], check=True)

if __name__ == "__main__":
    main()
