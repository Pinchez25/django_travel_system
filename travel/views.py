from django.views.generic import ListView, DetailView
from .models import SitePhotos, Video
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


def image_details(request):
    if request.method == "GET":
        photoid = request.GET.get('photoid')

        photo = get_object_or_404(SitePhotos, pk=int(photoid))

        return JsonResponse({
            'photo_url': photo.photo.url,
            'title': photo.title,
            'decription': str(photo.description)[20],
        })


class PhotoListView(ListView):
    model = SitePhotos
    template_name = 'homepage.html'
    context_object_name = 'photos'


class PhotoDetailView(DetailView):
    model = SitePhotos
    template_name = 'details.html'
    context_object_name = 'photo'


class VideoListView(ListView):
    model = Video
    template_name = 'videos.html'
    context_object_name = 'videos'


class VideoDetailView(DetailView):
    model = Video
    template_name = 'video-details.html'
    context_object_name = 'video'
