from __future__ import unicode_literals
from mongoengine import fields,DynamicDocument,EmbeddedDocument,DynamicEmbeddedDocument


class ToolInput(DynamicEmbeddedDocument):
    name = fields.StringField()
    value = fields.DynamicField()


class Tool(DynamicDocument):
    sender = fields.StringField(required=True)
    description = fields.StringField(required=True)
    priority = fields.IntField(required=True)
    datetime = fields.DateTimeField(required=True)
    inputs = fields.ListField(fields.EmbeddedDocumentField(ToolInput))
    fields.DynamicField()





