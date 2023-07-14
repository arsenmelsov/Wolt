from django.urls import path
from .views import basket_list, basket_detail, basket_new, basket_edit, basket_delete

urlpatterns = [
    path('', basket_list, name='basket_list'),
    path('/<int:pk>/', basket_detail, name='basket_detail'),
    path('/new/', basket_new, name='basket_new'),
    path('/<int:pk>/edit/', basket_edit, name='basket_edit'),
    path('/<int:pk>/delete/', basket_delete, name='basket_delete'),
    ]