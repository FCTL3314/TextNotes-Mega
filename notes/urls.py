from django.urls import path, include

from notes.views import NotesTemplateView

app_name = "notes"

urlpatterns = [
    path("api/", include("notes.api.urls", namespace="api")),
    path("", NotesTemplateView.as_view(), name="notes"),
]
