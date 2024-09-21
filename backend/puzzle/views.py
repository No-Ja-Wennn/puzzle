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

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def postFunction(request):
    data = request.body
    print(data)
    data = [
        [[1, 2, 4],
        [4, 5, 6],
        [7, 8, 0]],

        [[1, 2, 4],
        [4, 5, 6],
        [7, 8, 0]],
        
        [[1, 2, 4],
        [4, 5, 6],
        [7, 8, 0]],
        
    ]
    obj = {
        "array": data
    }
    return JsonResponse(obj)
