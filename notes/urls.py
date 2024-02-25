from django.urls import path, include

app_name = "notes"

urlpatterns = [
    path("api/", include("notes.api.urls", namespace="api")),
]
