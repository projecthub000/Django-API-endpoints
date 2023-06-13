# project/urls.py

from django.urls import include, path

urlpatterns = [
    # Other URL patterns
    path('api/', include('profiles.urls')),
]
