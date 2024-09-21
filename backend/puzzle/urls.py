from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.send),
    path('get/', views.index),
    path('post/', views.postFunction),
]
