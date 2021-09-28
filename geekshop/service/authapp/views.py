import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from service.authapp.models import User


def authentication(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        user = User.objects.filter(login=data['login'], password=data['password'])
        if user:
            return JsonResponse({'status': 'Аутентификация Пройдена'}, status=200)
        return JsonResponse({'status': 'Аутентификация Провалена'}, status=400)


def authorization(request):
    if request.method == 'POST':
        return JsonResponse({'status': 'Авторизация'})
