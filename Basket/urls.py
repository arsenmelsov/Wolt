from django.urls import path
from .views import basket_list, basket_detail, basket_new, basket_edit, basket_delete

urlpatterns = [
    path('baskets/', basket_list, name='basket_list'),
    path('basket/<int:pk>/', basket_detail, name='basket_detail'),
    path('basket/new/', basket_new, name='basket_new'),
    path('basket/<int:pk>/edit/', basket_edit, name='basket_edit'),
    path('basket/<int:pk>/delete/', basket_delete, name='basket_delete'),
    ]