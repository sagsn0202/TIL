from django.urls import path
from . import views

app_name = 'mton'

urlpatterns = [
    path('', views.enrollment_list, name='enrollment_list'),
    path('search/', views.search_lecture, name='search_lecture'),
]