from django.urls import include, path
from rest_framework_mongoengine import routers
from .django_app import views

router = routers.DefaultRouter()
router.register(r'api', views.ToolViewSet, base_name='api')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls))
]