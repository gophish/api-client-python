from gophish.models import Group
from gophish.api import APIEndpoint


class API(APIEndpoint):
    def __init__(self, api, endpoint='api/groups/'):
        super(API, self).__init__(api, endpoint=endpoint, cls=Group)

    def get(self, group_id=None):
        """ Gets one or more groups """
        return super(API, self).get(resource_id=group_id)

    def post(self, group):
        """ Creates a new group """
        return super(API, self).post(group)

    def put(self, group):
        """ Edits a group """
        return super(API, self).put(group)

    def delete(self, group_id):
        """ Deletes a group by ID """
        return super(API, self).delete(group_id)
