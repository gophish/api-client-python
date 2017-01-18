class API(object):
    def __init__(self, api, endpoint='/templates'):
        self.api = api
        self.endpoint = endpoint

    def get(template_id=None):
        """ Gets one or more templates """
        raise NotImplementedError

    def post(template):
        """ Creates a new template """
        raise NotImplementedError

    def put(template):
        """ Edits a template """
        raise NotImplementedError

    def delete(template_id):
        """ Deletes a template by ID """
        raise NotImplementedError
