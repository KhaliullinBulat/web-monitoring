from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('make_request/', make_request, name='make_request'),
]
