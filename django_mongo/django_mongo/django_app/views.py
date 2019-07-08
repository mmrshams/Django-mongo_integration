from rest_framework_mongoengine import viewsets

from .models import Tool
from .serializers import ToolSerializer


class ToolViewSet(viewsets.ModelViewSet):

    serializer_class = ToolSerializer

    def get_queryset(self):
        return Tool.objects.all()

