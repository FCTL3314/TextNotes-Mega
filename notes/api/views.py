from rest_framework import status
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.response import Response

from notes.models import TextNote


class TextNoteCreateAPIView(CreateAPIView):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class TextNoteDeleteAPIView(DestroyAPIView):
    def delete(self, request, *args, **kwargs):
        ids = request.GET.getlist("ids")
        deleted_notes = []
        for note_id in ids:
            try:
                note = TextNote.objects.get(id=note_id)
                note.delete()
                deleted_notes.append(note_id)
            except TextNote.DoesNotExist:
                pass
        return Response({"deleted_notes": deleted_notes})
