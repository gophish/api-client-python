from gophish.models import SMTP
from gophish.api import APIEndpoint

class API(APIEndpoint):
    def __init__(self, api, endpoint='/api/smtp/'):
        super(API, self).__init__(api, endpoint=endpoint, cls=SMTP)

    def get(self, smtp_id=None):
        """ Gets one or more SMTP sending profiles """

        return super(API, self).get(resource_id=smtp_id)

    def post(self, smtp):
        """ Creates a new SMTP sending profile """

        return super(API, self).post(smtp)

    def put(self, smtp):
        """ Edits an SMTP sending profile """

        return super(API, self).put(smtp)

    def delete(self, smtp_id):
        """ Deletes an SMTP sending profile by ID """

        return super(API, self).delete(smtp_id)
