from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # This URL pattern maps the root URL to the index view in views.py
    # Add more URL patterns here as needed
]