from django.urls import path
from .views import rest, callapi

urlpatterns = [
    path('', rest, name='rest'),
    path('callapi/', callapi, name='callapi'),
]