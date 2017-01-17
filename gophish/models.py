from datetime import datetime
import json as _json

class Model(object):
    def __init__(self):
        self.__valid_properties = {}

    @classmethod
    def parse(cls, json):
        """Parse a JSON object into a model instance."""
        raise NotImplementedError


class Campaign(Model):
    __valid_properties = {
        'id': None, 'name': None, 'created_date': datetime.now(),
        'launch_date': datetime.now(), 'completed_date': None, 'template': None,
        'page': None, 'results': [], 'status': None, 'timeline': [],
        'smtp': None, 'url': None}

    def __init__(self, **kwargs):
        """ Creates a new campaign instance """
        for key, default in Campaign.__valid_properties.items():
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
                timeline = [TimelineEntry.parse(entry) for entry in val]
                setattr(campaign, key, timeline)
            elif key == 'template':
                setattr(campaign, key, Template.parse(val))
            elif key == 'page':
                setattr(campaign, key, Page.parse(val))
            elif key == 'smtp':
                setattr(campaign, key, SMTP.parse(val))
            elif key in cls.__valid_properties:
                setattr(campaign, key, val)
        return campaign


class Result(Model):
    __valid_properties = {
            'id': None, 'first_name': None, 'last_name': None, 'email': None,
            'position': None, 'ip': None, 'latitude': None, 'longitude': None,
            'status': None}

    def __init__(**kwargs):
        for key, default in Result.__valid_properties.items():
            setattr(self, key, kwargs.get(key, default))

    @classmethod
    def parse(cls, json):
        raise NotImplementedError


class TimelineEntry(object):
    __valid_properties = ['email', 'time', 'message', 'details']

    def __init__(entry):
        for key, default in TimelineEntry.__valid_properties.items():
            setattr(self, key, kwargs.get(key, default))

    @classmethod
    def parse(cls, json):
        entry = cls()
        for key, val in json.items():
            if key == 'details':
                details = _json.loads(val)
                setattr(entry, key, details)
            elif key in cls.__valid_properties:
                setattr(entry, key, val)

    @classmethod
    def parse(cls, json):
        raise NotImplementedError


class User(Model):
    """ User contains the attributes for a member of a group
        used in Gophish """
    __valid_properties = {
            'id': None, 'first_name': None, 'last_name': None, 'email': None,
            'position': None}

    def __init__(**kwargs):
        for key, default in User.__valid_properties.items():
            setattr(self, key, kwargs.get(key, default))

    @classmethod
    def parse(cls, json):
        raise NotImplementedError


class Group(Model):
    """ Groups contain one or more users """
    _valid_properties = {
            'id': None, 'name': None, 'modified_date': datetime.now(),
            'targets': []}

    def __init__(**kwargs):
        for key, default in Group.__valid_properties.items():
            setattr(self, key, kwargs.get(key, default))

    @classmethod
    def parse(cls, json):
        group = cls()
        for key, val in json.items():
            if key == 'targets':
                users = [User.parse(user) for user in val]
                setattr(group, key, users)
            elif key == 'modified_date':
                setattr(group, key, parse_date(val))
            elif key in Group.__valid_properties:
                setattr(group, key, val)
        return group


class SMTP(Model):
    __valid_properties = {
        'id': None, 'interface_type': 'SMTP', 'name': None, 'host': None,
        'from_address': None, 'ignore_cert_errors' : False,
        'modified_date': datetime.now()}

    def __init__(**kwargs):
        for key, default in SMTP.__valid_properties.items():
            setattr(self, key, kwargs.get(key, default))

    @classmethod
    def parse(cls, json):
        smtp = cls()
        for key, val in json.items():
            if key == 'modified_date':
                setattr(smtp, key, parse_date(val))
            elif key in SMTP.__valid_properties:
                setattr(smtp, key, val)
        return smtp


class Template(Model):
    __valid_properties = {
        'id': None, 'name': None, 'text': None, 'html': None,
        'modified_date': datetime.now(), 'subject': None, 'attachments': []}

    def __init__(**kwargs):
        for key, default in Template.__valid_properties.items():
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
            elif key in Template.__valid_properties:
                setattr(template, key, val)


class Page(Model):
    __valid_properties = {
        'id': None, 'name': None, 'html': None, 'modified_date': datetime.now(),
        'capture_credentials': False, 'capture_passwords': False,
        'redirect_url': None}

    def __init__(**kwargs):
        for key, default in Page.__valid_properties.items():
            setattr(self, key, kwargs.get(key, default))

    @classmethod
    def parse(cls, json):
        page = cls()
        for key, val in json.items():
            if key == 'modified_date':
                setattr(page, key, parse_date(val))
            elif key in Page.__valid_properties:
                setattr(page, key, val)
