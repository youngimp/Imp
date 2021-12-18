from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def game(request):
    return render(request, 'main/game.html')


def AU(request):
    return render(request, 'main/AU.html')


def PS(request):
    return render(request, 'main/PS.html')


def register(request):
    return render(request, 'main/register.html')


def XBOX(request):
    return render(request, 'main/XBOX.html')


def pay(request):
    return render(request, 'main/pay.html')


def PC(request):
    return render(request, 'main/PC.html')


def news(request):
    return render(request, 'main/news.html')


def auth(request):
    return render(request, 'main/auth.html')

