from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('<int:id>',views.detail,name='detail'),
    path('addCart',views.addCart,name='addCart')
]