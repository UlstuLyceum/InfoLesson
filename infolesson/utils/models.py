# pylint: skip-file

from pymongo import MongoClient
from umongo import Document, Instance, fields

try:
    import infolesson.local_config as config
except ImportError:
    import infolesson.example_config as config

db = MongoClient(config.DB_HOST)[config.DB_NAME]
instance = Instance(db)


@instance.register
class User(Document):

    login = fields.StringField(required=True, unique=True)
    password = fields.StringField(required=True)
    name = fields.StringField()
    surname = fields.StringField()

    school = fields.ListField(fields.ReferenceField("School"))

    def has_perm(self, perm):
        pass


@instance.register
class School(Document):

    name = fields.StringField(required=True)
