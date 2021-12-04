from django.http import HttpResponse
from django.template.loader import render_to_string
from documents.models import Document


def home_view(req):
    objqs = Document.objects.all()
    context = {
        'objqs': objqs
    }
    return HttpResponse(render_to_string('home_view.html', context=context))
