from gophish.models import Group

class API(APIEndpoint):
    def __init__(self, api, endpoint='/groups'):
        super(API, self).__init__(api, endpoint=endpoint, cls=Group)

    def get(group_id=None):
        """ Gets one or more groups """
        return super(API, self).get(resource_id=group_id)

    def post(group):
        """ Creates a new group """
        return super(API, self).post(group)

    def put(group):
        """ Edits a group """
        return super(API, self).put(group)

    def delete(group_id):
        """ Deletes a group by ID """
        return super(API, self).put(group_id)
