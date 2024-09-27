from django.shortcuts import render
from Run import RUN
from state import State
# Create your views here.
from django.http import JsonResponse, HttpResponse
import json

def send(request):
    data = {
        "ten" : "hoang anh tus"
    }
    return JsonResponse(data)


def index(request):
     return HttpResponse("<h1>app iss runing</h1>")

def flatten_2d_array(two_d_array):
    one_d_array = []
    for row in two_d_array:
        for element in row:
            one_d_array.append(element)
    return one_d_array

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
@csrf_exempt
def postFunction(request):
    if request.method == 'POST':
        try:
            # data = json.loads(request.body)
            # data = flatten_2d_array(data['array'])  # Sử dụng get để tránh KeyError
            # print(data)
            data = [1, 5, 3, 4, 2, 6, 7, 8, 0]

            
            G = State() # nghe bạn đi
            S = G.clone()
            S.data = data
            G.data = [1, 2, 3, 4, 5 , 6, 7, 8, 0]
            RUN(S, G)
            print(RUN(S, G))
            result = {"data": 'Run.RUN(S, G)'}
            return JsonResponse(result)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        except KeyError:
            return JsonResponse({"error": "Missing 'array' key"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    
    return JsonResponse({"error": "Invalid request method"}, status=405)