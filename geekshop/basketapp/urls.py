from django.urls import path
import basketapp.views as basketapp

app_name = 'authapp'

app_name = 'authapp'
urlpatterns = [
    path('view/', basket, name='view'),
    path('add/<int:pk>', basket_add, name='add'),
    path('remove/', basket_remove, name='remove'),
    path('edit/<int:pk>/<int:quantity>', basketapp.basket_edit, name='edit'),
]
