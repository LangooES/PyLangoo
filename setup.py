"""
file: setup.py

Setup.py file for lit.
"""
import os
import shutil
import subprocess
import sys
from pathlib import Path

from setuptools import setup, find_packages
from setuptools.command.build_py import build_py

RESET_COLOR = "\x1b[39m"
RED = "\x1b[31m"
BLUE = "\x1b[34m"
YELLOW = "\x1b[33m"

BRIGHT = " \x1b[1m"
NORMAL = "\x1b[22m"


def red(s):
    return RED + s + RESET_COLOR


def blue(s):
    return BLUE + s + RESET_COLOR


def yellow(s):
    return YELLOW + s + RESET_COLOR


def bold(s):
    return BRIGHT + s + NORMAL


def err(msg):
    sys.stderr.write(red(f"Error: {msg}\n"))
    sys.exit(1)


def do_release_version_check():
    release_version = os.environ.get("RELEASE_VERSION")
    if not release_version:
        err("Failed to pick up release version from env var: RELEASE_VERSION")
    return release_version


def get_version():
    if os.environ.get("PYLANGOO_DO_RELEASE"):
        print(blue("PYLANGOO_DO_RELEASE is set, doing version check from environment"))
        return do_release_version_check()
    version = "0.1.0a0"
    return version


setup(
    name="pylangoo",
    version=get_version(),
    author="The Langoo Python Team",
    author_email="pablo@langoo.io",
    url="https://github.com/LangooES/PyLangoo/",
    packages=find_packages(),
    include_package_data=True,
    install_requires="requirements.txt",
    python_requires=">=3.10",
)
