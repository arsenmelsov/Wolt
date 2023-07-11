from django.urls import path
from .views import food_list, food_detail, food_new, food_edit, food_delete

urlpatterns = [
    path('foods/', food_list, name='food_list'),
    path('food/<int:pk>/', food_detail, name='food_detail'),
    path('food/new/', food_new, name='food_new'),
    path('food/<int:pk>/edit/', food_edit, name='food_edit'),
    path('food/<int:pk>/delete/', food_delete, name='food_delete'),
    ]