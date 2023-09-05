from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('register/create', views.CreateRegister.as_view(), name='createRegister'),
    path('register/list', views.ListRegisterActive.as_view(), name='listRegister'),
    path('register/update/<pk>', views.FinishRegister.as_view(), name='FinishRegister'),
]
