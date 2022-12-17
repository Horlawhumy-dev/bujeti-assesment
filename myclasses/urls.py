
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('classrooms', views.get_classrooms, name='classrooms'),
    # path('fetch_classrooms', views.FetchClassroomsView.as_view(), name="fetch_classrooms"),
]
