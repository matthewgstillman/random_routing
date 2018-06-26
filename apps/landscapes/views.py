from django.shortcuts import render, redirect
from random import random
# Create your views here.
def index(request):
    return render(request, 'landscapes/index.html')

def result(request, id):
    id = int(str(id))
    if int(id) in range(1,10):
        src = "../static/img/snowy.jpg"
    if int(id) in range(11,20):
        src = "../static/img/desert.jpg"
    if int(id) in range(21,30):
        src = "../static/img/forest.jpg"
    if int(id) in range(31,40):
        src = "../static/img/vineyard.jpg"
    if int(id) in range(41,50):
        src = "../static/img/tropical.jpg"
    context = {
    'src': src,
    # 'src': src
    }
    return render(request, 'landscapes/result.html', context)

def random(request, id):
    random_num = random.randint(1,50);
    id = int(str(random_num))
    if int(id) in range(1,10):
        src = "../static/img/snowy.jpg"
    if int(id) in range(11,20):
        src = "../static/img/desert.jpg"
    if int(id) in range(21,30):
        src = "../static/img/forest.jpg"
    if int(id) in range(31,40):
        src = "../static/img/vineyard.jpg"
    if int(id) in range(41,50):
        src = "../static/img/tropical.jpg"
    context = {
    'src': src,
    'id': int(id)
    }
    return render(request, 'landscapes/result.html', context)
