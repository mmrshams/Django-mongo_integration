from django.urls import include, path
from rest_framework_mongoengine import routers
from .django_app import views

router = routers.DefaultRouter()
router.register(r'api', views.ToolViewSet, base_name='api')

# http://localhost:8000/api/  send post request for data validation and store
urlpatterns = [
    path('', include(router.urls))
]