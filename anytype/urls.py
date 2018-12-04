from django.urls import path

from .views import _config, _DataUploadView

_upload = _DataUploadView.as_view()

urlpatterns = [
    path('<int:project_id>/config/', _config),
    path('<int:project_id>/upload/', _upload),
]
