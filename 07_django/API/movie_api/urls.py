from django.urls import path
from . import views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='영화 api')

urlpatterns = [
    path('', schema_view),
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/<int:movie_id>/', views.selected_movie, name='selected_movie'),
]
