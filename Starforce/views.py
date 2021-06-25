from django.shortcuts import render
from main import calculate

def button(request):
    return render(request, 'home.html')

def output(request):
    data = calculate(0, 17, 160, safeguard=False, event=None)
    print(data)
    return render(request, 'home.html')