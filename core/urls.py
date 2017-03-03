from django.conf.urls import url
from core import views

patterns = [
    url(r'^$', views.index, name='index')
]