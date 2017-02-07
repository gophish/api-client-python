import json

from gophish.models import Campaign, Error
from gophish.api import APIEndpoint


class API(APIEndpoint):
    def __init__(self, api, endpoint='/api/campaigns/'):
        """ Creates a new instance of the campaigns API """

        super(API, self).__init__(api, endpoint=endpoint, cls=Campaign)

    def get(self, campaign_id=None):
        """ Gets the details for one or more campaigns by ID """

        return super(API, self).get(resource_id=campaign_id)

    def post(self, campaign):
        """ Creates a new campaign """

        return super(API, self).post(campaign)

    def puts(self, campaign):
        """ Edits an existing campaign """

        return super(API, self).put(campaign)

    def delete(self, campaign_id):
        """ Deletes an existing campaign """

        return super(API, self).delete(campaign_id)

    def complete(self, campaign_id):
        """ Complete an existing campaign (Stop processing events) """

        return super(API, self).get(resource_id=campaign_id, 
                                    resource_action='complete')

    def summary(campaign_id=None):
        """ Returns the summary of one or more campaigns. """
        raise NotImplementedError

    def results(campaign_id):
        """ Returns just the results for a given campaign """
        raise NotImplementedError
