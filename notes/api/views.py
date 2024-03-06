from django.http import JsonResponse
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
        ids_string = request.GET.get("ids", "")
        ids = ids_string.split(",")

        notes_to_delete = TextNote.objects.filter(id__in=ids)

        deleted_notes_count = notes_to_delete.delete()
        return JsonResponse({"deleted_notes_count": deleted_notes_count})
