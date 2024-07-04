from setuptools import setup

with open ("README.md", "r", encoding="utf-8") as fh:
   long_description = fh.read()
AUTHOR_NAME = 'NISHTHA'
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['sreamlit' ]
setup(
    name = SRC_REPO,
    version = '0.0.1',
    author = 'NISHTHA',
    author_email = 'nishthahooda10@gmail.com',
    description = 'A small example package for movies recommendation',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    package = [SRC_REPO],
    python_requires = '>=3.7',
    install_requires = LIST_OF_REQUIREMENTS,
    )
