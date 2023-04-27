from django.urls import path
from . import views

app_name = 'tienda'

urlpatterns = [
    path('', views.index, name='index'),
    path('producto/<int:producto_id>/', views.producto, name='producto'),
    path('gaseosas/', views.gaseosas, name='gaseosas'),
    path('chocolates/', views.chocolates, name='chocolates'),
    path('galletas/', views.galletas, name='galletas'),
    path('snacks/', views.snacks, name='snacks')
]