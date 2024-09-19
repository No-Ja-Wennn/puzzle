from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.send),
    path('get/', views.index)
]
