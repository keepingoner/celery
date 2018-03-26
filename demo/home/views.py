# from django.shortcuts import render
#
# # Create your views here.
from django.http import HttpResponse
from home import tasks


def index(request):
    x = request.GET.get('x', '')
    y = request.GET.get('y', '')
    s = tasks.sayhello.delay()

    return HttpResponse('+++{}+++{}++++{}--{}-{}-{}'.format(s, s.id, s.successful(), s.failed(), s.get(), s.ready()))