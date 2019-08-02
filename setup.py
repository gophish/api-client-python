"""This is the setup module for the Python Gophish API client."""
from setuptools import setup

setup(
    name="gophish",
    packages=["gophish", "gophish.api"],
    version="0.3.0",
    description="Python API Client for Gophish",
    author="Jordan Wright",
    author_email="python@getgophish.com",
    url="https://github.com/gophish/api-client-python",
    license="MIT",
    download_url="https://github.com/gophish/api-client-python/tarball/0.3.0",
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
        "appdirs==1.4.0",
        "packaging==16.8",
        "pyparsing==2.1.10",
        "python-dateutil==2.6.0",
        "requests>=2.20.0",
        "six==1.10.0",
    ],
)
