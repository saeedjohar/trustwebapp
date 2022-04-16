from unicodedata import name
from django.urls import path
from . import views

# URL ConfCould not connect to "": password authentication failed for user ""Could not connect to "": password authentication failed for user ""
urlpatterns = [
    path('', views.index, name='rules'),
    path('index', views.index, name='index'),
    path('hello', views.hello, name='hello'),
   
]