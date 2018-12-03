from django.urls import path

from .views import (_ListProject, _CreateProject, _DetailProject, _DeleteProject)

_list = _ListProject.as_view()
_create = _CreateProject.as_view()
_detail = _DetailProject.as_view()
_delete = _DeleteProject.as_view()

urlpatterns = [
    path('', _list),
    path('create/', _create),
    path('detail/<int:pk>/', _detail),
    path('delete/<int:pk>/', _delete),
]
