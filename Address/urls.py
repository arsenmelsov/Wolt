from django.urls import path
from .views import address_list, address_detail, address_new, address_edit, address_delete

urlpatterns = [
    path('', address_list, name='address_list'),
    path('/<int:pk>/', address_detail, name='address_detail'),
    path('/new/', address_new, name='address_new'),
    path('/<int:pk>/edit/', address_edit, name='address_edit'),
    path('/<int:pk>/delete/', address_delete, name='address_delete'),
    ]