from django.http import HttpResponse

def home_view(req):
    return HttpResponse("hollo")