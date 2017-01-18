import requests

DEFAULT_URL = 'http://localhost:3333'

class Gophish:
    def __init__(self, api_key, host=DEFAULT_URL):
        self.api_key = api_key
        self.host = host
    
    def __execute(path, method, data=None):
        """ Executes a request to a given endpoint, returning the result """

        url = "{}/{}".format(this.host, path)
        response = requests.request(method, url, json=data)
        return response.json()
