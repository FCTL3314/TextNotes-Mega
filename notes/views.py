from django.views.generic import TemplateView


class NotesTemplateView(TemplateView):
    template_name = "notes/notes.html"
