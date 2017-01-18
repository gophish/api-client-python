import requests

'''
api.py 

Base API endpoint class that abstracts basic CRUD operations.
'''

class APIEndpoint:
    """
    Represents an API endpoint for Gophish, containing common patterns
    for CRUD operations.
    """
    def __init__(self, api, endpoint=None):
        """ Creates an instance of the APIEndpoint class.

        Args:
            api - Gophish.client - The authenticated REST client
            endpoint - str - The URL path to the resource endpoint
        """
        self.api = api
        self.endpoint = endpoint

    def get(self, cls, resource_id=None):
        """ Gets the details for one or more resources by ID
        
        Args:
            cls - gophish.models.Model - The resource class
            resource_id - str - The endpoint (URL path) for the resource

        Returns:
            One or more instances of cls parsed from the returned JSON
        """

        endpoint = self.endpoint

        if resource_id:
            endpoint = '{}/{}'.format(endpoint, resource_id)

        response = self.api.execute("GET", endpoint)
        if not response.ok:
            return Error.parse(response.json())

        if resource_id:
            return cls.parse(response.json())

        return [cls.parse(resource) for resource in response.json()]

    def post(self, cls, resource):
        """ Creates a new instance of the resource.

        Args:
            cls - gophish.models.Model - The resource class

        """
        response = self.api.execute("POST", self.endpoint, json=json.dumps(resource))
        
        if not response.ok:
            return Error.parse(response.json())

        return cls.parse(response.json())

    def put(self, cls, resource):
        """ Edits an existing resource

        Args:
            cls - gophish.models.Model - The resource class
            resource - gophish.models.Model - The resource instance
        """
        
        endpoint = self.endpoint

        if resource.id:
            endpoint = '{}/{}'.format(endpoint, resource.id)

        response = self.api.execute("PUT", endpoint, json=resource.as_json())

        if not respose.ok:
            return Error.parse(response.json())

        return cls.parse(response.json())

    def delete(self, cls, resource_id):
        """ Deletes an existing resource

        Args:
            cls - gophish.models.Model - The resource class
            resource_id - int - The resource ID to be deleted
        """

        endpoint = '{}/{}'.format(self.endpoint, resource_id)

        response = self.api.execute("DELETE", endpoint)

        if not response.ok:
            return Error.parse(response.json())

        return cls.parse(response.json())
