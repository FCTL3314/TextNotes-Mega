from django.db import models
from django.utils import timezone


class TextNote(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    mega_path = models.FilePathField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now_add=timezone.now)

    def __str__(self) -> str:
        return self.text if len(self.text) < 60 else f"{self.text[:60]}..."
