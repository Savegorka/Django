from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Basket
from mainapp.models import Product
# Create your views here.

def basket(request):
    content = {}
    return render(request, 'basketapp/basket.html', content)

def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket = Basket.objects.filter(user=request.user, pk=pk)

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket[0].quantity += 1
    basket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def basket_remove(request):
    basket = Basket.objects.filter(user=request.user, pk=pk)
    basket[0].quantity -= 1
    basket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
