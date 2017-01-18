class API(object):
    def __init__(self, api, endpoint='/smtp'):
        self.api = api
        self.endpoint = endpoint

    def get(smtp_id=None):
        """ Gets one or more SMTP sending profiles """
        raise NotImplementedError

    def post(smtp):
        """ Creates a new SMTP sending profile """
        raise NotImplementedError

    def put(smtp):
        """ Edits an SMTP sending profile """
        raise NotImplementedError

    def delete(smtp_id):
        """ Deletes an SMTP sending profile by ID """
        raise NotImplementedError
