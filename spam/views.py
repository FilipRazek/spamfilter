from django.http import HttpResponse
from .spam_filter import run_spam_filter


def index(request):
    run_spam_filter()
    return HttpResponse("Hello, world. You're at the polls index.")
