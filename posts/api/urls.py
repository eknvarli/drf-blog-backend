from django.urls import path
from posts.api.views import *

urlpatterns = [
    path('list', PostListAPIView.as_view(), name='list')
]