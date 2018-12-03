from django.urls import path

from .views import _config

urlpatterns = [
    path('<int:project_id>/config/', _config),
]
