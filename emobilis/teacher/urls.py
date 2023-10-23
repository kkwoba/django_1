from django.urls import path

from .import views

urlpattern=[
    path('',views.home)
    path('about', views.about)
    path('contact',views.contact)
]