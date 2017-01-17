import json

from gophish.error import Error
from gophish.models import Campaign


class API(object):
    def __init__(self, api, endpoint='/campaigns'):
        """ Creates a new instance of the campaigns API """
        self.api = api
        self.endpoint = endpoint

    def get(campaign_id=None):
        """ Gets the details for one or more campaigns. """

        endpoint = self.endpoint

        if campaign_id:
            endpoint = '{}/{}'.format(endpoint, campaign_id)

        response = self.api.execute("GET", endpoint)
        if not response.ok:
            return error.Error(response.json())

        if campaign_id:
            return Campaign.parse(response.json())
        return [
            Campaign.parse() for campaign_json in response.json()]

    def post(campaign):
        """ Creates a new campaign """
        raise NotImplementedError


    def summary(campaign_id=None):
        """ Returns the summary of one or more campaigns. """
        raise NotImplementedError

    def results(campaign_id=None):
        raise NotImplementedError
