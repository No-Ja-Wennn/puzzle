from django.shortcuts import render
import copy
import json
from django.http import HttpResponse, JsonResponse
# Create your views here.

# start = [[2, 8, 3],
#          [1, 6, 4],
#          [7,"", 5]]

# goal =  [[1, 2, 3],
#          [8, "", 4],
#          [7, 6, 5]]

def seach(start):
    for i in range(len(start)):
        for j in range(len(start)):
            if start[i][j] == "":
                return (i, j)

def top(u, row, col):
    if row <= 0:
        return None
    u[row][col] = u[row-1][col]
    u[row - 1][col] = ""
    return u

def buttom(u, row, col):
    if row >= 2:
        return None
    u[row][col] = u[row + 1][col]
    u[row + 1][col] = ""
    return u

def left(u, row, col):
    if col <= 0: 
        return None
    u[row][col] = u[row][col - 1]
    u[row][col - 1] = ""
    return u

def right(u, row, col):
    if col >= 2:
        return None
    u[row][col] = u[row][col + 1]
    u[row][col + 1] = ""
    return u


def All_case(u, row, col):
    arr = []
    u_tmp = copy.deepcopy(u)
    tmp = top(u_tmp, row, col)
    if tmp != None:
        arr.append(tmp)
    u_tmp = copy.deepcopy(u)
    tmp = buttom(u_tmp, row, col)
    if tmp != None:
        arr.append(tmp)
    u_tmp = copy.deepcopy(u)
    tmp = left(u_tmp, row, col)
    if tmp != None:
        arr.append(tmp)
    u_tmp = copy.deepcopy(u)
    tmp = right(u_tmp, row, col)
    if tmp != None:
        arr.append(tmp)
    return arr

def h(v, goal):
    count = 0
    for row in range(len(v)):
        for col in range(len(v)):
            if v[row][col] != "" and v[row][col] != goal[row][col]:
                count += 1
    return count  

def remove_by_h(way):
    g_temp = 0
    temp_array = []
    for index in range(len(way)):
        if g_temp == way[index]['g']:
            temp_array.append(way[index])
            g_temp += 1
        
        
    return temp_array
                  

def A_function(start, goal):
    g = 0
    L = [{
        "f":0,
        "g":0,
        "values": start
    }] 
    visited = [start]
    way = [{
        "g": 0,
        "values": start
    }]

    while True:
        # if 
        if len(L) == 0:
            print("that bai!")
            return []
        u = L.pop(0)

        way.append(u)
        
        if u["values"] == goal:
            print("thanh cong")
            way = remove_by_h(way)
            return way
        row, col = seach(u["values"])
        g = u["g"] + 1
        for v in All_case(u["values"], row, col):
            
            if v not in visited:
                visited.append(v)
                f_val = g + h(v, goal)
                L.append({"g":g, "h":h(v, goal), "f":f_val, "values":v})

        L = sorted(L, key=lambda x: x["f"])

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Nếu đây là API, dùng csrf_exempt để tránh lỗi CSRF
def index(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)['data']  # Đọc dữ liệu từ request body
            start = data["start"]
            goal = data["goal"]
            print(start)
            print(goal)
            # Giả sử A_function xử lý dữ liệu và trả về kết quả
            result = A_function(start, goal)
            
            # Trả về kết quả dưới dạng JSON response
            return JsonResponse({'result': result}, status=200)
        
        except KeyError:
            return JsonResponse({'error': 'Invalid data format'}, status=400)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)
