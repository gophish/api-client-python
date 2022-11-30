from datetime import datetime
from dateutil.tz import tzlocal

import json as _json
import dateutil.parser


def parse_date(datestr):
    """ Parses an ISO 8601 formatted date from Gophish """
    return dateutil.parser.parse(datestr)


class Model(object):
    def __init__(self):
        self._valid_properties = {}

    @classmethod
    def _is_builtin(cls, obj):
        return isinstance(obj, (int, float, str, list, dict, bool))

    def as_dict(self):
        """ Returns a dict representation of the resource """
        result = {}
        for key in self._valid_properties:
            val = getattr(self, key)
            if isinstance(val, datetime):
                val = val.isoformat()
            # Parse custom classes
            elif val and not Model._is_builtin(val):
                val = val.as_dict()
            # Parse lists of objects
            elif isinstance(val, list):
                # We only want to call as_dict in the case where the item
                # isn't a builtin type.
                for i in range(len(val)):
                    if Model._is_builtin(val[i]):
                        continue
                    val[i] = val[i].as_dict()
            # If it's a boolean, add it regardless of the value
            elif isinstance(val, bool):
                result[key] = val

            # Add it if it's not None
            if val:
                result[key] = val
        return result

    @classmethod
    def parse(cls, json):
        """Parse a JSON object into a model instance."""
        raise NotImplementedError


class Campaign(Model):
    _valid_properties = {
        'id': None,
        'name': None,
        'created_date': datetime.now(tzlocal()),
        'launch_date': datetime.now(tzlocal()),
        'send_by_date': None,
        'completed_date': None,
        'template': None,
        'page': None,
        'results': [],
        'status': None,
        'timeline': [],
        'smtp': None,
        'url': None,
        'groups': [],
    }

    def __init__(self, **kwargs):
        """ Creates a new campaign instance """
        for key, default in Campaign._valid_properties.items():
            setattr(self, key, kwargs.get(key, default))

    @classmethod
    def parse(cls, json):
        campaign = cls()
        for key, val in json.items():
            # TODO Add date parsing
            if key == 'results':
                results = [Result.parse(result) for result in val]
                setattr(campaign, key, results)
            elif key == 'timeline':
                if val is not None:
                    timeline = [TimelineEntry.parse(entry) for entry in val]
                    setattr(campaign, key, timeline)
            elif key == 'template':
                setattr(campaign, key, Template.parse(val))
            elif key == 'page':
                setattr(campaign, key, Page.parse(val))
            elif key == 'smtp':
                setattr(campaign, key, SMTP.parse(val))
            elif key in cls._valid_properties:
                setattr(campaign, key, val)
        return campaign


class CampaignSummaries(Model):
    ''' Represents a list of campaign summary objects '''
    _valid_properties = {'total': None, 'campaigns': None}

    def __init__(self):
        """ Creates a new instance of the campaign summaries"""
        for key, default in CampaignSummaries._valid_properties.items():
            setattr(self, key, default)

    @classmethod
    def parse(cls, json):
        campaign_summaries = cls()
        for key, val in json.items():
            # TODO Add date parsing
            if key == 'campaigns':
                summaries = [CampaignSummary.parse(summary) for summary in val]
                setattr(campaign_summaries, key, summaries)
            elif key in cls._valid_properties:
                setattr(campaign_summaries, key, val)
        return campaign_summaries


class CampaignSummary(Model):
    ''' Represents a campaign summary object '''
    _valid_properties = {
        'id': None,
        'name': None,
        'status': None,
        'created_date': None,
        'send_by_date': None,
        'launch_date': None,
        'completed_date': None,
        'stats': None
    }

    def __init__(self):
        for key, default in CampaignSummary._valid_properties.items():
            setattr(self, key, default)

    @classmethod
    def parse(cls, json):
        summary = cls()
        for key, val in json.items():
            # TODO Add date parsing
            if key == 'stats':
                stats = Stat.parse(val)
                setattr(summary, key, stats)
            elif key in cls._valid_properties:
                setattr(summary, key, val)
        return summary


class Stat(Model):
    _valid_properties = {
        'total': None,
        'sent': None,
        'opened': None,
        'clicked': None,
        'submitted_data': None,
        'email_reported': None,
        'error': None
    }

    def __init__(self):
        for key, default in Stat._valid_properties.items():
            setattr(self, key, default)

    @classmethod
    def parse(cls, json):
        stat = cls()
        for key, val in json.items():
            if key in cls._valid_properties:
                setattr(stat, key, val)
        return stat


class CampaignResults(Model):
    ''' Represents a succinct view of campaign results '''
    _valid_properties = {
        'id': None,
        'name': None,
        'results': [],
        'status': None,
        'timeline': [],
    }

    def __init__(self, **kwargs):
        """ Creates a new instance of the campaign results object"""
        for key, default in CampaignResults._valid_properties.items():
            setattr(self, key, kwargs.get(key, default))

    @classmethod
    def parse(cls, json):
        campaign_results = cls()
        for key, val in json.items():
            # TODO Add date parsing
            if key == 'results':
                results = [Result.parse(result) for result in val]
                setattr(campaign_results, key, results)
            elif key == 'timeline':
                if val is not None:
                    timeline = [TimelineEntry.parse(entry) for entry in val]
                    setattr(campaign_results, key, timeline)
            elif key in cls._valid_properties:
                setattr(campaign_results, key, val)
        return campaign_results


class Result(Model):
    _valid_properties = {
        'id': None,
        'first_name': None,
        'last_name': None,
        'email': None,
        'position': None,
        'ip': None,
        'latitude': None,
        'longitude': None,
        'status': None
    }

    def __init__(self, **kwargs):
        for key, default in Result._valid_properties.items():
            setattr(self, key, kwargs.get(key, default))

    @classmethod
    def parse(cls, json):
        result = cls()
        for key, val in json.items():
            if key in cls._valid_properties:
                setattr(result, key, val)
        return result


class TimelineEntry(Model):
    _valid_properties = {
        'email': None,
        'time': None,
        'message': None,
        'details': None
    }

    def __init__(self):
        ''' Creates a new instance of a timeline entry '''
        for key, default in TimelineEntry._valid_properties.items():
            setattr(self, key, default)

    @classmethod
    def parse(cls, json):
        entry = cls()
        for key, val in json.items():
            if key == 'details' and val != "":
                details = _json.loads(val)
                setattr(entry, key, details)
            elif key in cls._valid_properties:
                setattr(entry, key, val)
        return entry


class User(Model):
    """ User contains the attributes for a member of a group
        used in Gophish """
    _valid_properties = {
        'id': None,
        'first_name': None,
        'last_name': None,
        'email': None,
        'position': None
    }

    def __init__(self, **kwargs):
        for key, default in User._valid_properties.items():
            setattr(self, key, kwargs.get(key, default))

    @classmethod
    def parse(cls, json):
        user = cls()
        for key, val in json.items():
            if key in cls._valid_properties:
                setattr(user, key, val)
        return user


class Group(Model):
    """ Groups contain one or more users """
    _valid_properties = {
        'id': None,
        'name': None,
        'modified_date': datetime.now(tzlocal()),
        'targets': []
    }

    def __init__(self, **kwargs):
        for key, default in Group._valid_properties.items():
            setattr(self, key, kwargs.get(key, default))

    @classmethod
    def parse(cls, json):
        group = cls()
        for key, val in json.items():
            if key == 'targets':
                targets = [User.parse(user) for user in val]
                setattr(group, key, targets)
            elif key == 'modified_date':
                setattr(group, key, parse_date(val))
            elif key in cls._valid_properties:
                setattr(group, key, val)
        return group


class SMTP(Model):
    _valid_properties = {
        'id': None,
        'interface_type': 'SMTP',
        'name': None,
        'host': None,
        'username': None,
        'password': None,
        'from_address': None,
        'ignore_cert_errors': False,
        'modified_date': datetime.now(tzlocal()),
        'headers': []
    }

    def __init__(self, **kwargs):
        for key, default in SMTP._valid_properties.items():
            setattr(self, key, kwargs.get(key, default))

    @classmethod
    def parse(cls, json):
        smtp = cls()
        for key, val in json.items():
            if key == 'modified_date':
                setattr(smtp, key, parse_date(val))
            elif key in cls._valid_properties:
                setattr(smtp, key, val)
        return smtp


class Template(Model):
    _valid_properties = {
        'id': None,
        'name': None,
        'text': None,
        'html': None,
        'modified_date': datetime.now(tzlocal()),
        'subject': None,
        'attachments': []
    }

    def __init__(self, **kwargs):
        for key, default in Template._valid_properties.items():
            setattr(self, key, kwargs.get(key, default))

    @classmethod
    def parse(cls, json):
        template = cls()
        for key, val in json.items():
            if key == 'modified_date':
                setattr(template, key, parse_date(val))
            elif key == 'attachments' and val:
                attachments = [
                    Attachment.parse(attachment) for attachment in val
                ]
                setattr(template, key, attachments)
            elif key in cls._valid_properties:
                setattr(template, key, val)
        return template


class Page(Model):
    _valid_properties = {
        'id': None,
        'name': None,
        'html': None,
        'modified_date': datetime.now(tzlocal()),
        'capture_credentials': False,
        'capture_passwords': False,
        'redirect_url': None
    }

    def __init__(self, **kwargs):
        for key, default in Page._valid_properties.items():
            setattr(self, key, kwargs.get(key, default))

    @classmethod
    def parse(cls, json):
        page = cls()
        for key, val in json.items():
            if key == 'modified_date':
                setattr(page, key, parse_date(val))
            elif key in cls._valid_properties:
                setattr(page, key, val)
        return page


class Attachment(Model):
    _valid_properties = {'content': None, 'type': None, 'name': None}

    @classmethod
    def parse(cls, json):
        attachment = cls()
        for key, val in json.items():
            if key in cls._valid_properties:
                setattr(attachment, key, val)
        return attachment


class Webhook(Model):
    _valid_properties = {
        'id': None,
        'name': None,
        'url': None,
        'secret': None,
        'is_active': None
    }

    def __init__(self, **kwargs):
        for key, default in Webhook._valid_properties.items():
            setattr(self, key, kwargs.get(key, default))

    @classmethod
    def parse(cls, json):
        webhook = cls()
        for key, val in json.items():
            if key in cls._valid_properties:
                setattr(webhook, key, val)
        return webhook


class IMAP(Model):
    _valid_properties = {
        'enabled': None,
        'host': None,
        'port': None,
        'username': None,
        'password': None,
        'tls': None,
        'folder': None,
        'restrict_domain': None,
        'delete_reported_campaign_email': None,
        'last_login': None,
        'modified_date': None,
        'imap_freq': None
    }

    def __init__(self, **kwargs):
        for key, default in IMAP._valid_properties.items():
            setattr(self, key, kwargs.get(key, default))

    @classmethod
    def parse(cls, json):
        imap = cls()
        for key, val in json.items():
            if key in cls._valid_properties:
                setattr(imap, key, val)
        return imap


class Success(Exception, Model):
    _valid_properties = {'message': None, 'success': None, 'data': None}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.message

    @classmethod
    def parse(cls, json):
        success = cls()
        for key, val in json.items():
            if key in cls._valid_properties:
                setattr(success, key, val)
        return success


class Error(Exception, Model):
    _valid_properties = {'message': None, 'success': None, 'data': None}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.message

    def __repr__(self):
        return _json.dumps(self.as_dict())

    @classmethod
    def parse(cls, json):
        error = cls()
        for key, val in json.items():
            if key in cls._valid_properties:
                setattr(error, key, val)
        return error
