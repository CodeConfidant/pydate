#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='pydate',
    version='1.1.7',
    packages=find_packages(),
    license='MIT',
    description='Package made to format date & time strings for use in various SQL RDBMS',
    long_description=open('README.txt').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/CodeConfidant/pydate-time',
    author='Drew Hainer',
    author_email='codeconfidant@gmail.com',
    platforms=['Windows', 'Linux']
)

# - Update README.md and README.txt
# - Update Version Number
# - Tar Wrap the Package: python setup.py sdist
# - Upload to PYPI: twine upload dist/*
# - Commit Changes
# - Change Release Version in Github Repo