from rest_framework import status
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from notes.api.serializers import TextNoteDeleteManySerializer, TextNoteSerializer
from notes.models import TextNote


class TextNoteCreateAPIView(CreateAPIView):
    serializer_class = TextNoteSerializer

    def create(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class TextNoteDeleteAPIView(DestroyAPIView):
    serializer_class = TextNoteDeleteManySerializer

    def delete(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        ids = serializer.validated_data["ids"]
        TextNote.objects.filter(id__in=ids).delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
