from django.urls import path
from cadastro.views import index

urlpatterns = [
    path('index/', index),
]