from django.urls import path
from mainapp.views import products, contact, product

urlpatterns = [
    path('products/', products, name='products'),
    path('product-page/<int:pk>/', product, name="product-page"),
    path('contact/', contact, name='contact'),
]