from django.shortcuts import render
from .models import Document


def doc_search_view(req):
    try:
        q = int(req.GET.get('q'))
    except:
        q = None
    obj = None
    if q is not None:
        obj = Document.objects.get(id=q)
    context = {
        'obj': obj
    }
    return render(req, 'documents/search_view.html', context=context)


def doc_create_form(req):
    context = {}
    if req.method == 'POST':
        title = req.POST.get('title')
        content = req.POST.get('content')
        obj = Document.objects.create(title=title, content=content)
        context['obj'] = obj
        context['created'] = True
    return render(req, 'documents/create_form.html', context=context)


def doc_detail_view(req, id):
    obj = Document.objects.get(id=id)
    context = {
        'obj': obj
    }
    return render(req, 'documents/detail_view.html', context=context)

