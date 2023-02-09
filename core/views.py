from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(req, name, age):
    return HttpResponse("<h1>Hello {} {} years old</h1>".format(name, age))
