from django.urls import path
from .views import order_list, order_detail, order_new, order_edit, order_delete

urlpatterns = [
    path('orders/', order_list, name='order_list'),
    path('order/<int:pk>/', order_detail, name='order_detail'),
    path('order/new/', order_new, name='order_new'),
    path('order/<int:pk>/edit/', order_edit, name='order_edit'),
    path('order/<int:pk>/delete/', order_delete, name='order_delete'),
    ]