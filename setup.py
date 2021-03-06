import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="indenter",
    version="1.0.1",
    description="Indent text using `with` blocks",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/glacials/indenter",
    author="Ben Carlsson",
    author_email="qhiiyr@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    packages=["indenter"],
)
