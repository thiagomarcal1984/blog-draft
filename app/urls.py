from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post-list'),
    path('<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-update'),
    path('new/', views.PostCreateView.as_view(), name='post-create'),
]
