from django.db import models
from django.core.validators import FileExtensionValidator


class SitePhotos(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Site Photos'
        db_table = "Photos"


class Video(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/%Y/%m/%d/', validators=[
        FileExtensionValidator(allowed_extensions=['mp4', 'avi',
                                                   'mov', 'wmv', 'flv', 'mkv', 'webm', '3gp', '3g2', 'm4v',
                                                   'mpeg', 'mpg', 'mpe', 'mpv', 'm2v', 'm4v', 'svi', '3gp', '3g2',
                                                   'mxf', 'roq', 'nsv', 'f4v', 'f4p', 'f4a', 'f4b'])
    ])
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Videos'
        db_table = "Videos"
