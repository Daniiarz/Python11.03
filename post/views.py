from datetime import datetime

from django.http import HttpResponse


def hello_world_view(request):
    return HttpResponse("Hello, World!")


def date_view(request):
    now = datetime.now()
    return HttpResponse(str(now))
