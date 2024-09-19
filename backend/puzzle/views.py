from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponse

def send(request):
    data = {
        'name': "Hoang Anh Tu",
        'age': 18
    }
    return JsonResponse(data)


def index(request):
     return HttpResponse("<h1>app iss runing</h1>")