from django.urls import path
from . import views

app_name = 'monitoring'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('nodes/', views.nodes_list, name='nodes_list'),
    path('contacts/', views.contacts, name='contacts'),
    path('health/', views.health_check, name='health'),
]
