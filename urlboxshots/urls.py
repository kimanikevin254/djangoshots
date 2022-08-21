from django.urls import path

from . import views

urlpatterns = [
    path('', views.urlbox),
    path('result/', views.result),
]
