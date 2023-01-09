"""ESHOP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import home, signup, login, cart, checkout, myorders
urlpatterns = [
    path('signup', signup.Signup.as_view()),
    path('login', login.Login.as_view(), name="login"),
    path('logout', login.logout),
    path('myorders', myorders.Myorders.as_view()),
    path('cart', cart.Cart.as_view(), name='cart'),
    path('checkout', checkout.Checkout.as_view()),
    path('', home.Index.as_view(), name='homepage')
]
