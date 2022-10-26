"""Package configuration."""
from setuptools import setup

setup(
    name="scrape_boyt",
    version="0.1",
    packages=["scrape_boyt"],
    package_dir={"": "src"},
    install_requires=["pytest==7.1.3", "black==22.10.0"],
)
