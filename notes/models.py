from django.db import models
from django.utils import timezone


class TextNote(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.text if len(self.text) < 60 else f"{self.text[:60]}..."
