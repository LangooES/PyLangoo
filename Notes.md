# Python Packages

## Glossary

#### Distribution Package
A versioned archive file that contains Python packages, modules, and other resource files that are used to distribute a Release. The archive file is what an end-user will download from the internet and install.

#### Built Distribution
A Distribution format containing files and metadata that only need to be moved to the correct location on the target system, to be installed. Wheel is such a format, whereas distutil’s Source Distribution is not, in that it requires a build step before it can be installed. This format does not imply that Python files have to be precompiled (Wheel intentionally does not include compiled Python files).

#### Source Distributions
A distribution format (usually generated using python setup.py sdist) that provides metadata and the essential source files needed for installing by a tool like pip, or for generating a Built Distribution.

#### Wheels
A Built Distribution format introduced by PEP 427, which is intended to replace the Egg format. Wheel is currently supported by pip.

#### Release
A snapshot of a Project at a particular point in time, denoted by a version identifier.

Making a release may entail the publishing of multiple Distributions. For example, if version 1.0 of a project was released, it could be available in both a source distribution format and a Windows installer distribution format.

## Development Mode
[Documentation][Devmode]
You can perform a pip installation passing the -e/--editable flag (e.g., pip install -e .).   
It works very similarly to pip install ., except that it doesn’t actually install anything. Instead, it creates a special .egg-link file in the target directory (usually site-packages) that links to your project’s source code. It may also update an existing easy-install.pth file to include your project’s source code, thereby making it available on sys.path for all programs using that Python installation.





[Devmode]: https://setuptools.pypa.io/en/latest/userguide/development_mode.html