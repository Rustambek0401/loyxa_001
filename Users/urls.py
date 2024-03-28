from django.urls import path
from .views import index, index2

urlpatterns = [
    path('index/', index),
    path('index2/', index2),
]