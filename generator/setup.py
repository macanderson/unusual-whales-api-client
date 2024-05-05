import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="unusual-whales-api-client",
    author="",
    version="0.0.2",
    description="A client library for accessing Unusual Whales API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.12.2",
    install_requires=["httpx >= 0.20.0, < 0.28.0", "attrs >= 21.3.0", "python-dateutil >= 2.8.0, < 3"],
    package_data={"unusual_whales_api_client": ["py.typed"]},
)
