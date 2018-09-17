from django.urls import path, include
from .views import publicacion, CreatePostView

urlpatterns = [
	path('publicaciones/', publicacion, name='post'),
	path('crear/', CreatePostView.as_view(), name='post-create'),
]