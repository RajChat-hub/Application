from setuptools import setup, find_packages

setup(
    name='rcxproj',
    version='2.0',
    description='A build system for C++ projects similar to VCXProj',
    author='Rajdeep Chatterjee', 
    author_email='rc9775295@gmail.com',
    url='https://github.com/RajChat-hub',  # URL of the project 
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'rcx=rcxproj.cli:main',
        ],
    },
    install_requires=[
        'lxml',
    ],
)