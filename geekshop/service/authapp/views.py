from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.


def authentication(request):
    if request.method == 'POST':
        return JsonResponse({'status': 'Аутентификация'})


def authorization(request):
    if request.method == 'POST':
        return JsonResponse({'status': 'Авторизация'})
