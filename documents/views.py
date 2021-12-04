from django.shortcuts import render
from .models import Document


def doc_detail_view(req, id):
    obj = Document.objects.get(id=id)
    context = {
        'obj': obj
    }
    return render(req, 'documents/detail_view.html', context=context)

