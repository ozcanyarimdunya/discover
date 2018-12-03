from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('project.urls')),
    path('p/', include('process.urls')),
    path('admin/', admin.site.urls),
]
