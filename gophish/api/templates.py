from gophish.models import Template
from gophish.api import APIEndpoint


class API(APIEndpoint):
    def __init__(self, api, endpoint='api/templates/'):
        super(API, self).__init__(api, endpoint=endpoint, cls=Template)

    def get(self, template_id=None):
        """ Gets one or more templates """

        return super(API, self).get(resource_id=template_id)

    def post(self, template):
        """ Creates a new template """

        return super(API, self).post(template)

    def put(self, template):
        """ Edits a template """

        return super(API, self).put(template)

    def delete(self, template_id):
        """ Deletes a template by ID """

        return super(API, self).delete(template_id)
