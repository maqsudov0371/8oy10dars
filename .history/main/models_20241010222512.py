from django.db import models


from django.core.exceptions import ValidationError

ALLOWED_VIDEO_TYPES = ['video/mp4', 'video/mkv']
MAX_FILE_SIZE = 52428800  # 50 MB

def video_upload(instance, filename):
    return f'videos/{filename}'

class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_file = models.FileField(upload_to=video_upload)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_file = models.FileField(upload_to=video_upload)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.video_file.size > MAX_FILE_SIZE:
            raise ValidationError('Fayl hajmi 50 MB dan oshmasligi kerak!')
        if self.video_file.file.content_type not in ALLOWED_VIDEO_TYPES:
            raise ValidationError('Faqat MP4 va MKV formatlari ruxsat etilgan!')
