from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('project.urls')),
    path('a/', include('anytype.urls')),
    path('admin/', admin.site.urls),
]
