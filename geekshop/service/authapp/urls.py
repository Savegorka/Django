from django.urls import path
from .views import authorization, authentication

urlpatterns = [
    path('authentication/', authentication),
    path('authorization', authorization),
]