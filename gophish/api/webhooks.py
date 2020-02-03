from gophish.models import Webhook
from gophish.api import APIEndpoint


class API(APIEndpoint):
    def __init__(self, api, endpoint='api/webhooks/'):
        super(API, self).__init__(api, endpoint=endpoint, cls=Webhook)

    def get(self, webhook_id=None):
        """Gets one or more webhooks

        Keyword Arguments:
            webhook_id {int} --  The ID of the Webhook (optional, default: {None})
        """

        return super(API, self).get(resource_id=webhook_id)

    def post(self, webhook):
        """Creates a new webhook

        Arguments:
            webhook {gophish.models.Webhook} -- The webhook to create
        """

        return super(API, self).post(webhook)

    def put(self, webhook):
        """Edits a webhook

        Arguments:
            webhook {gophish.models.Webhook} -- The updated webhook details
        """

        return super(API, self).put(webhook)

    def delete(self, webhook_id):
        """Deletes a webhook by ID

        Arguments:
            webhook_id {int} -- The ID of the webhook to delete
        """
        return super(API, self).delete(webhook_id)

    def validate(self, webhook_id):
        """Sends a validation payload to the webhook specified by the given ID

        Arguments:
            webhook_id {int} -- The ID of the webhook to validate
        """
        return self.request("POST",
                            resource_id=webhook_id,
                            resource_action='validate',
                            resource_cls=Webhook,
                            single_resource=True)
