from __future__ import unicode_literals
from mongoengine import fields,DynamicDocument,EmbeddedDocument,DynamicEmbeddedDocument


class ToolInput(DynamicEmbeddedDocument):
    """
    this is  for store the embed json or list of json objects inside main part
    """
    name = fields.StringField()
    value = fields.DynamicField()


class Tool(DynamicDocument):
    """
    main part of json with dynamic filed that our input can be scalable and store any range of data
    """
    sender = fields.StringField(required=True)
    description = fields.StringField(required=True)
    priority = fields.IntField(required=True)
    datetime = fields.DateTimeField(required=True)
    inputs = fields.ListField(fields.EmbeddedDocumentField(ToolInput))
    # dynamic filed:
    fields.DynamicField()





