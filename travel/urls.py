from django.urls import path
from .views import PhotoListView, PhotoDetailView, VideoListView, VideoDetailView, image_details

urlpatterns = [
    path('', PhotoListView.as_view(), name='photo-list'),
    path('photo/<int:pk>/', PhotoDetailView.as_view(), name='photo-detail'),
    path('video/', VideoListView.as_view(), name='video-list'),
    path('video/<int:pk>/', VideoDetailView.as_view(), name='video-detail'),
    path('image-details/', image_details, name='image-details'),
]
