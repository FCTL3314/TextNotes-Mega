from django.urls import path

from notes.api.views import TextNoteCreateAPIView, TextNoteDeleteAPIView

app_name = "notes"

urlpatterns = [
    path("notes/create/", TextNoteCreateAPIView.as_view(), name="note_create"),
    path("notes/delete/", TextNoteDeleteAPIView.as_view(), name="note_delete"),
]
