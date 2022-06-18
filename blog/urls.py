from django.urls import path
from blog.views import blogview

urlpatterns = [
    path('', blogview, name='blog'),
]