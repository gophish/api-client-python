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
        "certifi==2020.6.20",
        "chardet==3.0.4",
        "idna==2.10",
        "packaging==20.4",
        "pyparsing==2.4.7",
        "python-dateutil==2.8.1",
        "requests==2.24.0",
        "six==1.15.0",
        "urllib3==1.25.10"
    ],
)
