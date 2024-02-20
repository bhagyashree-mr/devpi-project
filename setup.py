# devpi_project/setup.py
from setuptools import setup, find_packages

setup(
    name='devpi_project',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'hello-cli = devpi_project.hello:say_hello',
        ],
    },
)

