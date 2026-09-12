from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PostFeaturedListView

app_name = 'core'

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/nuevo/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/editar/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/eliminar/', PostDeleteView.as_view(), name='post-delete'),
    path('destacados/', PostFeaturedListView.as_view(), name='post-featured-list'),
]