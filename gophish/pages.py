class API(object):
    def __init__(self, api, endpoint='/pages'):
        self.api = api
        self.endpoint = endpoint

    def get(page_id=None):
        """ Gets one or more pages """
        raise NotImplementedError

    def post(page):
        """ Creates a new page """
        raise NotImplementedError

    def put(page):
        """ Edits a page """
        raise NotImplementedError

    def delete(page_id):
        """ Deletes a page by ID """
        raise NotImplementedError
