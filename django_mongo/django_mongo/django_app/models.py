from __future__ import unicode_literals
from mongoengine import Document, fields


class Tool(Document):
    sender = fields.StringField(required=True)
    description = fields.StringField(required=True)
    priority = fields.IntField(required=True)
    datetime = fields.DateTimeField(required=True)





