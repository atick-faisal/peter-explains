from setuptools import setup, find_packages

from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="peter-explains",
    version="0.0.2",
    description="Linux command explanations from Peter Griffin",
    author="Atick Faisal",
    author_email="atickfaisal@gmail.com",
    packages=find_packages(),
    install_requires=[],
    long_description=long_description,
    long_description_content_type="text/markdown",
)