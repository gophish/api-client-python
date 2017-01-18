class API(object):
    def __init__(self, api, endpoint='/groups'):
        self.api = api
        self.endpoint = endpoint

    def get(group_id=None):
        """ Gets one or more groups """
        raise NotImplementedError

    def post(group):
        """ Creates a new group """
        raise NotImplementedError

    def put(group):
        """ Edits a group """
        raise NotImplementedError

    def delete(group_id):
        """ Deletes a group by ID """
        raise NotImplementedError
