from django.urls import path
from . import views
urlpatterns = [
    path('', views.login,name='login'),
    path('checkLogin',views.checkLogin,name='checkLogin'),
    path('signup',views.signup,name='signup')
]