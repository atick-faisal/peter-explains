from pathlib import Path
from setuptools import setup, find_packages
from peter_explains import _version

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="peter-explains",
    version=_version.__version__,
    description="Linux command explanations from Peter Griffin",
    author="Atick Faisal",
    author_email="atickfaisal@gmail.com",
    packages=find_packages(),
    install_requires=["colorama", "diskcache", "json_repair", "google-generativeai"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": [
            "peter = peter_explains.main:peter",
        ],
    },
    url="https://github.com/atick-faisal/peter-explains",
    license="MIT",
)
