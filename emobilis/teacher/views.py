from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Home(request):
    return HttpResponse("welcome to emobilis")


class HttpsResponse("welcome to emobilis"):


def about(request):
    return HttpsResponse("about emobilis")

def contact(request):
    return HttpsResponse("asante")