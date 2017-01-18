import json

from gophish.error import Error
from gophish.models import Campaign
from gophish.api import APIEndpoint


class API(APIEndpoint):
    def __init__(self, api, endpoint='/campaigns'):
        """ Creates a new instance of the campaigns API """
        super(API, self).__init__(api, endpoint=endpoint)

    def summary(campaign_id=None):
        """ Returns the summary of one or more campaigns. """
        raise NotImplementedError

    def results(campaign_id):
        """ Returns just the results for a given campaign """
        raise NotImplementedError
