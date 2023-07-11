from django.urls import path
from .views import city_list, city_detail, city_new, city_edit, city_delete

urlpatterns = [
    path('citys/', city_list, name='city_list'),
    path('city/<int:pk>/', city_detail, name='city_detail'),
    path('city/new/', city_new, name='city_new'),
    path('city/<int:pk>/edit/', city_edit, name='city_edit'),
    path('city/<int:pk>/delete/', city_delete, name='city_delete'),
    ]