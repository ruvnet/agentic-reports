from setuptools import setup, find_packages
import os

def post_install():
    # Set PYTHONPATH to include the project root directory
    os.environ['PYTHONPATH'] = os.environ.get('PYTHONPATH', '') + ':/workspaces/agentic-reports/project-root'

    # Ensure the correct working directory
    os.chdir('/workspaces/agentic-reports/project-root')

    # Run Uvicorn with the necessary parameters
    os.system('uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 --reload-dir /workspaces/agentic-reports/project-root')

setup(
    name='agentic-reports',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'fastapi',
        'pydantic',
        'pandas',
        'exa_py',
        'pytest',
        'uvicorn',
        'pydantic_settings',
    ],
    entry_points={
        'console_scripts': [
            'agentic-reports=setup:post_install',
        ],
    },
)
