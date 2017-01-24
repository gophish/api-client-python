# Gophish Python API Client

Gophish was built from the ground-up to be API-first. This means that we build out the API endpoints for all of our features, and the UI is simply a wrapper around these endpoints.

To interface with Gophish using Python, we've created a `gophish` client library.

> If you want to access the API directly, please refer to our [API Documentation](https://www.gitbook.com/book/gophish/api-documentation/details)

## Installation

To install the `gophish` library, simply run the command:

`pip install gophish`

## Quickstart

Getting up and running with the Python library is quick and easy.

To start, simply create a client using the API key found in the [Settings page](https://gophish.gitbooks.io/user-guide/content/documentation/changing_user_settings.html#changing-your-password--updating-settings).

```python
from gophish import Gophish

api_key = 'API_KEY'
api = Gophish(api_key)
```

Now you're ready to start using the API!

## Full Documentation

You can find the full Python client documentation [here.](https://gophish.gitbooks.io/python-api-client/content/)
