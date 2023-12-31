from django.urls import path
from .views import food_list, food_detail, food_new, food_edit, food_delete

urlpatterns = [
    path('', food_list, name='food_list'),
    path('/<int:pk>/', food_detail, name='food_detail'),
    path('/new/', food_new, name='food_new'),
    path('/<int:pk>/edit/', food_edit, name='food_edit'),
    path('/<int:pk>/delete/', food_delete, name='food_delete'),
    ]