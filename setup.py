"""
file: setup.py

Setup.py file for lit.
"""

from setuptools import setup, find_packages

setup(
    name="pylangoo",
    version="0.1.0",
    author="The Langoo Python Team",
    author_email="pablo@langoo.io",
    # url="https://github.com/LangooES/PyLangoo/",
    packages=find_packages(),
    python_requires=">=3.10",
)
