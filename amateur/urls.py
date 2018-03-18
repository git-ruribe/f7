from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('phone/', views.phone, name='phone'),
    path('guardamsg/', views.guardamsg, name='guardamsg'),
]
