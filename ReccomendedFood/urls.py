from django.urls import path
from .views import reccomendedFood_list, reccomendedFood_detail, reccomendedFood_new, reccomendedFood_edit, reccomendedFood_delete

urlpatterns = [
    path('', reccomendedFood_list, name='reccomendedFood_list'),
    path('/<int:pk>/', reccomendedFood_detail, name='reccomendedFood_detail'),
    path('/new/', reccomendedFood_new, name='reccomendedFood_new'),
    path('/<int:pk>/edit/', reccomendedFood_edit, name='reccomendedFood_edit'),
    path('/<int:pk>/delete/', reccomendedFood_delete, name='reccomendedFood_delete'),
    ]