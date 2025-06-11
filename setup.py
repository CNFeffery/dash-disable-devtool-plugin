from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")
setup(
    name="dash-disable-devtool-plugin",
    version="0.1.0",
    install_requires=[
        "dash>=3.0.4",
    ],
    packages=["dash_disable_devtool_plugin"],
    author="CNFeffery",
    author_email="fefferypzy@gmail.com",
    description="A plugin to disable browser developer tools and other page operation permissions for Dash applications using Dash Hooks.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CNFeffery/dash-disable-devtool-plugin",
)
