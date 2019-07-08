
from rest_framework_mongoengine import serializers

from .models import Tool


class ToolSerializer(serializers.DynamicDocumentSerializer):
    """
    validation data  base on django models requirement
    """
    class Meta:
        model = Tool
        fields = '__all__'
