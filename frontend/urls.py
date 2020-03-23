from django.urls import path
from . import views

app_name = 'Eckmo-frontend'

urlpatterns = [
    path('', views.index),
]

