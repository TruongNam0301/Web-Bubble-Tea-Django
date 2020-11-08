from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('delete',views.deleteCart,name='deletecart'),
    path('order',views.order,name='order')
]