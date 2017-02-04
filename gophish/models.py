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

    def as_dict(self):
        """ Returns a dict representation of the resource """
        result = {}
        for key in self._valid_properties:
            val = getattr(self, key)
            if isinstance(val, datetime):
                val = val.isoformat()
            # Parse custom classes
            elif val and not isinstance(val, (str, list, dict)):
                val = val.as_dict()
            # Parse lists of objects
            elif isinstance(val, list):
                val = [e.as_dict() for e in val]

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
        'id': None, 'name': None, 'created_date': datetime.now(tzlocal()),
        'launch_date': datetime.now(tzlocal()), 'completed_date': None, 'template': None,
        'page': None, 'results': [], 'status': None, 'timeline': [],
        'smtp': None, 'url': None, 'groups': [], 'profile': None}

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


class Result(Model):
    _valid_properties = {
            'id': None, 'first_name': None, 'last_name': None, 'email': None,
            'position': None, 'ip': None, 'latitude': None, 'longitude': None,
            'status': None}

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


class TimelineEntry(object):
    _valid_properties = {'email': None, 'time': None, 'message': None, 'details': None}

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
            'id': None, 'first_name': None, 'last_name': None, 'email': None,
            'position': None}

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
            'id': None, 'name': None, 'modified_date': datetime.now(tzlocal()),
            'targets': []}

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
        'id': None, 'interface_type': 'SMTP', 'name': None, 'host': None,
        'from_address': None, 'ignore_cert_errors' : False,
        'modified_date': datetime.now(tzlocal())}

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
        'id': None, 'name': None, 'text': None, 'html': None,
        'modified_date': datetime.now(tzlocal()), 'subject': None, 'attachments': []}

    def __init__(self, **kwargs):
        for key, default in Template._valid_properties.items():
            setattr(self, key, kwargs.get(key, default))

    @classmethod
    def parse(cls, json):
        template = cls()
        for key, val in json.items():
            if key == 'modified_date':
                setattr(template, key, parse_date(val))
            elif key == 'attachments':
                attachments = [
                        Attachment.parse(attachment) for attachment in val]
                setattr(template, key, attachments)
            elif key in cls._valid_properties:
                setattr(template, key, val)
        return template


class Page(Model):
    _valid_properties = {
        'id': None, 'name': None, 'html': None, 'modified_date': datetime.now(tzlocal()),
        'capture_credentials': False, 'capture_passwords': False,
        'redirect_url': None}

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

class Error(Model):
    _valid_properties = {'message', 'success', 'data'}

    @classmethod
    def parse(cls, json):
        error = cls()
        for key, val in json.items():
            if key in cls._valid_properties:
                setattr(error, key, val)
        return error
