import pathlib

from setuptools import setup

README = (pathlib.Path(__file__).parent / "README.md").read_text()


def get_version(rel_path: str):
    file_path = pathlib.Path(__file__).parent.absolute() / rel_path
    for line in file_path.read_text().splitlines():
        if line.startswith("__version__"):
            return line.split('"')[1]
    raise RuntimeError("Unable to find version string.")


setup(
    name="binary4fun",
    version=get_version("src/binary4fun/__init__.py"),
    url="github...",
    author="Moritz Körber",
    author_email="moritz.koerber@gmail.com",
    description="A little game to guess numbers by means of binary search.",
    long_description=README,
    long_description_content_type="text/markdown",
    packages=["binary4fun"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)
