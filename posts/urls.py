from django.urls import path
from . import views

urlpatterns = [
    path('', views.CommunityPostList.as_view(), name='community-post-list'),
    path('<int:pk>/', views.CommunityPostDetail.as_view(), name='community-post-detail'),
]
