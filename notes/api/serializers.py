from rest_framework import serializers

from notes.models import TextNote


class TextNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextNote
        fields = ("id", "text", "title", "created_at", "updated_at")
