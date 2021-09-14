from django.shortcuts import render
import datetime
from mainapp.models import Product

def main(request):
    title = 'Главная'
    products = Product.objects.all()
    content = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', content)

def products(request):
    return render(request, 'mainapp/products.html')

def contact(request):
    return render(request, 'mainapp/contact.html')

def temp(request):
    return render(request, 'mainapp/temp1.html', {'data': datetime.datetime.now()})
