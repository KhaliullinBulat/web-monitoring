from django.urls import path
from .views import *

app_name = 'links'

urlpatterns = [
    path('status/', LinkView.as_view()),
    path('urls/', LinkCreate.as_view()),
    # path('links/', LinkListView.as_view(), name='link_list'),
    # path('links/<pk>/', views.LinkDetailView.as_view(), name='link_detail'),
]
