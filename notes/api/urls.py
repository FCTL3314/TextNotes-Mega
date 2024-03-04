from django.urls import path

from notes.api.views import TextNoteCreateAPIView

app_name = "notes"

urlpatterns = [
    path("textnotes/create/", TextNoteCreateAPIView.as_view(), name="textnote_create"),
]
