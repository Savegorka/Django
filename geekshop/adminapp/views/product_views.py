from django.shortcuts import get_object_or_404, render

from mainapp.models import ProductCategory, Product


def products(request, pk):
    title = 'админка/продукты'

    category = get_object_or_404(ProductCategory, pk=pk)
    product_list = Product.objects.filter(category__pk=pk).order_by('name')
    content = {
        'title': title,
        'category': category,
        'objects': product_list,

    }
    return render(request, '', content)


def product_create(request, pk):
    pass


def product_update(request, pk):
    pass


def product_delete(request, pk):
    pass