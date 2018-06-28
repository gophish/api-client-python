import requests

from gophish.models import Error
'''
api.py 

Base API endpoint class that abstracts basic CRUD operations.
'''


class APIEndpoint(object):
    """
    Represents an API endpoint for Gophish, containing common patterns
    for CRUD operations.
    """

    def __init__(self, api, endpoint=None, cls=None):
        """ Creates an instance of the APIEndpoint class.

        Args:
            api - Gophish.client - The authenticated REST client
            endpoint - str - The URL path to the resource endpoint
            cls - gophish.models.Model - The Class to use when parsing results
        """
        self.api = api
        self.endpoint = endpoint
        self._cls = cls

    def get(self,
            resource_id=None,
            resource_action=None,
            resource_cls=None,
            single_resource=False):
        """ Gets the details for one or more resources by ID
        
        Args:
            cls - gophish.models.Model - The resource class
            resource_id - str - The endpoint (URL path) for the resource
            resource_action - str - An action to perform on the resource
            resource_cls - cls - A class to use for parsing, if different than the base resource
            single_resource - bool - An override to tell Gophish that even 
                though we aren't requesting a single resource, we expect a single response object

        Returns:
            One or more instances of cls parsed from the returned JSON
        """

        endpoint = self.endpoint

        if not resource_cls:
            resource_cls = self._cls

        if resource_id:
            endpoint = '{}/{}'.format(endpoint, resource_id)

        if resource_action:
            endpoint = '{}/{}'.format(endpoint, resource_action)

        response = self.api.execute("GET", endpoint)
        if not response.ok:
            return Error.parse(response.json())

        if resource_id or single_resource:
            return resource_cls.parse(response.json())

        return [resource_cls.parse(resource) for resource in response.json()]

    def post(self, resource):
        """ Creates a new instance of the resource.

        Args:
            resource - gophish.models.Model - The resource instance

        """
        response = self.api.execute(
            "POST", self.endpoint, json=(resource.as_dict()))

        if not response.ok:
            return Error.parse(response.json())

        return self._cls.parse(response.json())

    def put(self, resource):
        """ Edits an existing resource

        Args:
            resource - gophish.models.Model - The resource instance
        """

        endpoint = self.endpoint

        if resource.id:
            endpoint = '{}/{}'.format(endpoint, resource.id)

        response = self.api.execute("PUT", endpoint, json=resource.as_json())

        if not response.ok:
            return Error.parse(response.json())

        return self._cls.parse(response.json())

    def delete(self, resource_id):
        """ Deletes an existing resource

        Args:
            resource_id - int - The resource ID to be deleted
        """

        endpoint = '{}/{}'.format(self.endpoint, resource_id)

        response = self.api.execute("DELETE", endpoint)

        if not response.ok:
            return Error.parse(response.json())

        return self._cls.parse(response.json())
