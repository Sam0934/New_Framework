from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def hello(request):
    text = """<h1> The Current Time is  %s</h1>""" %datetime.datetime.now()
    return HttpResponse(text)

def article(request, art_id):
    return  HttpResponse("<h1> The Aritcle which is called is %s </h1>"%art_id)

def rendering_file(request):
    """

    :param request:
    :return:
    """
    return render(request, "index.html", {})

def login(request):
    """

    :param request:
    :return:
    """
    return render(request, "user_form.html", {})
