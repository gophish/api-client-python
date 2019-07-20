from gophish.models import Page
from gophish.api import APIEndpoint


class API(APIEndpoint):
    def __init__(self, api, endpoint='api/pages/'):
        super(API, self).__init__(api, endpoint=endpoint, cls=Page)

    def get(self, page_id=None):
        """ Gets one or more pages """

        return super(API, self).get(resource_id=page_id)

    def post(self, page):
        """ Creates a new page """

        return super(API, self).post(page)

    def put(self, page):
        """ Edits a page """

        return super(API, self).put(page)

    def delete(self, page_id):
        """ Deletes a page by ID """

        return super(API, self).delete(page_id)
