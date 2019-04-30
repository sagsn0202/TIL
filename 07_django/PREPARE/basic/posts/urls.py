from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.posts_list, name='posts_list'),
    path('<int:post_pk>/', views.post_detail, name='post_detail'),
    path('create/', views.create_post, name='create_post'),
    path('<int:post_pk>/update/', views.update_post, name='update_post'),
    path('<int:post_pk>/delete/', views.delete_post, name='delete_post'),
    path('<int:post_pk>/toggle_like/', views.toggle_like, name='toggle_like'),
]
