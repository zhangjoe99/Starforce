from django.shortcuts import render
from ../pythons/main.py import calculate
from



def output(request):
    data = calculate(0, 17, 160, safeguard=False, event=None)
    print(data)
    return render(request, 'home.html')