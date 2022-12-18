
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('virtual_classroom/<str:pk>/', views.get_classroom, name='virtual_classroom'),
    path('login_teacher', views.login_teacher, name="login_teacher"),
    path('create_classroom', views.create_classroom, name="create_classroom"),
    path('delete_classroom/<str:pk>/', views.delete_classroom, name="delete_classroom"),
    path('update_classroom/<str:pk>/', views.update_classroom, name="update_classroom"),
]
