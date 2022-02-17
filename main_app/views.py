from django.shortcuts import render

# Create your views here.

class Plant:
    def __init__(self, name):
        self.name = name

plants = [
    Plant('Christmas Cactus'),
    Plant('Aloe'),
    Plant('Snake Plant')
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def plants_index(request):
    return render(request, 'plants/index.html', {'plants': plants})