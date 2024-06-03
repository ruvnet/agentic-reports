from setuptools import setup, find_packages
from pathlib import Path

def read_long_description():
    this_directory = Path(__file__).parent
    long_description = (this_directory / "README.md").read_text()
    return long_description

setup(
    name='agentic_reports',
    version='0.1.5',
    packages=find_packages(where='project-root'),
    package_dir={'': 'project-root'},
    py_modules=['start'],  # Include the start module
    install_requires=[
        'twine',
        'setuptools',
        'wheel',
        'flake8',
        'black',
        'pytest',
        'pip-upgrader',
        'fastapi',
        'uvicorn',
        'pandas',
        'pydantic',
        'exa_py',
        'pydantic-settings',
        'virtualenv',
        'litellm'
    ],
    python_requires='>=3.10',
    author='rUv',
    author_email='null@ruv.net',
    description='Agent Reporting using Exa.ai API.',
    long_description=read_long_description(),
    long_description_content_type='text/markdown',
    url='https://github.com/ruvnet/agentic-reports',
    license='Apache License 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
    ],
    entry_points={
        'console_scripts': [
            'agentic-reports=start:main',
        ],
    },
)
