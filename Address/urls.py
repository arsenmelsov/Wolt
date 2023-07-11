from django.urls import path
from .views import address_list, address_detail, address_new, address_edit, address_delete

urlpatterns = [
    path('addresss/', address_list, name='address_list'),
    path('address/<int:pk>/', address_detail, name='address_detail'),
    path('address/new/', address_new, name='address_new'),
    path('address/<int:pk>/edit/', address_edit, name='address_edit'),
    path('address/<int:pk>/delete/', address_delete, name='address_delete'),
    ]