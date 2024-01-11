"""This is the setup module for the Python Gophish API client."""
from setuptools import setup

setup(
    name="gophish",
    packages=["gophish", "gophish.api"],
    version="0.5.1",
    description="Python API Client for Gophish",
    author="Jordan Wright",
    author_email="python@getgophish.com",
    url="https://github.com/gophish/api-client-python",
    license="MIT",
    download_url="https://github.com/gophish/api-client-python/tarball/0.5.1",
    keywords=["gophish"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
    ],
    install_requires=[
        "appdirs==1.4.4",
        "certifi==2023.11.17",
        "chardet==5.2.0",
        "idna==3.6",
        "packaging==23.2",
        "pyparsing==3.1.1",
        "python-dateutil==2.8.2",
        "requests==2.31.0",
        "six==1.16.0",
        "urllib3==2.1.0"
    ],
)
