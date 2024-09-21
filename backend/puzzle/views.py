from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponse

def send(request):
    data = {
        "ten" : "hoang anh tus"
    }
    return JsonResponse(data)


def index(request):
     return HttpResponse("<h1>app iss runing</h1>")

# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 0]