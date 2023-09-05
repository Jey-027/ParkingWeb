from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('register/create', views.CreateRegister.as_view(), name='createRegister')
]
