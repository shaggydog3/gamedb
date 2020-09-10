from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the Fallout 76 Game DB index.")
