from django.urls import path
from .views import role_list, role_detail, role_new, role_edit, role_delete

urlpatterns = [
    path('', role_list, name='role_list'),
    path('/<int:pk>/', role_detail, name='role_detail'),
    path('/new/', role_new, name='role_new'),
    path('/<int:pk>/edit/', role_edit, name='role_edit'),
    path('/<int:pk>/delete/', role_delete, name='role_delete'),
    ]