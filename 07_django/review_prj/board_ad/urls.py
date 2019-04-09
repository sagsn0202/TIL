from django.urls import path
from . import views

app_name = 'board_ad'

urlpatterns = [
    path('create/', views.create_posting, name='create_posting'),
    path('', views.posting_list, name='posting_list'),
    path('<int:posting_id>/', views.posting_detail, name='posting_detail'),
    path('<int:posting_id>/update/', views.update_posting, name='update_posting'),
    path('<int:posting_id>/delete/', views.delete_posting, name='delete_posting'),
    path('<int:posting_id>/comments/create/', views.create_comment, name='create_comment'),
    path('<int:posting_id>/comments/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
]
