from django.urls import path

from notes.api.views import TextNoteCreateAPIView, TextNoteDeleteAPIView

app_name = "notes"

urlpatterns = [
    path("textnotes/create/", TextNoteCreateAPIView.as_view(), name="textnote_create"),
    path("textnotes/delete/", TextNoteDeleteAPIView.as_view(), name="textnote_delete"),
]
