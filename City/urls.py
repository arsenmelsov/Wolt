from django.urls import path
from .views import city_list, city_detail, city_new, city_edit, city_delete

urlpatterns = [
    path('/', city_list, name='city_list'),
    path('/<int:pk>/', city_detail, name='city_detail'),
    path('/new/', city_new, name='city_new'),
    path('/<int:pk>/edit/', city_edit, name='city_edit'),
    path('/<int:pk>/delete/', city_delete, name='city_delete'),
    ]