"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from task2.views import Class_view, func_view, index
from task3.views import ClassHome, ClassShop, ClassBasket, func_shop

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('func_view/', func_view),
    path('class_view/', Class_view.as_view()),
    path('platform/', ClassHome.as_view()),
    # path('platform/games/', ClassShop.as_view()),
    path('platform/games/', func_shop),
    path('platform/cart/', ClassBasket.as_view())
    ]
