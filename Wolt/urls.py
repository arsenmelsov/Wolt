"""
URL configuration for Wolt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('users/', include('Users.urls')),
    path('restaurants/', include('Restaurant.urls')), 
    path('orders/', include('Order.urls')),
    path('addresses/', include('Address.urls')),
    path('baskets/', include('Basket.urls')),
    path('foods/', include('Food.urls')),
    path('countries/', include('Country.urls')),
    path('cities/', include('City.urls')),
    path('courier/', include('Courier.urls')),
    path('branches/', include('Branch.urls')),
    path('branchAddress/', include('BranchAddress.urls')),
    path('cards/', include('Card.urls')),
    path('categories/', include('Category.urls')),
    path('houseTypes/', include('HouseType.urls')),
    path('reccomendedFoods/', include('ReccomendedFood.urls'))
]