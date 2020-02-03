from gophish.models import IMAP, Success
from gophish.api import APIEndpoint


class API(APIEndpoint):
    def __init__(self, api, endpoint='api/imap/'):
        super(API, self).__init__(api, endpoint=endpoint, cls=IMAP)

    def get(self):
        """Gets the configured IMAP settings
        """

        return super(API, self).get()

    def post(self, imap):
        """Updates the IMAP settings

        Arguments:
            imap {gophish.models.IMAP} -- The IMAP settings to configure
        """

        return super(API, self).post(imap)

    def validate(self, imap):
        """Sends a validation payload to the webhook specified by the given ID

        Arguments:
            webhook_id {int} -- The ID of the webhook to validate
        """
        return self.request("POST",
                            body=imap.as_dict(),
                            resource_action='validate',
                            resource_cls=Success,
                            single_resource=True)
