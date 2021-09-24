from django.shortcuts import render

from mainapp.models import ProductCategory


def categories(request):
    title = 'админка/категории'

    category_list = ProductCategory.objects.all()
    content = {
        'title': title,
        'objects': category_list,

    }
    return render(request, 'adminapp/categories.html', content)


def category_create(request, pk):
    pass


def category_update(request, pk):
    pass


def category_delete(request, pk):
    pass