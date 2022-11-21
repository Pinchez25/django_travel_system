from .models import Video


def get_video(request):
    video = Video.objects.all()
    return {'all_videos': video}
