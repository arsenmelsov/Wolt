from django.urls import path
from .views import rest_list, rest_detail, rest_new, rest_edit, rest_delete

urlpatterns = [
    path('', rest_list, name='rest_list'),
    path('/<int:pk>/', rest_detail, name='rest_detail'),
    path('/new/', rest_new, name='rest_new'),
    path('/<int:pk>/edit/', rest_edit, name='rest_edit'),
    path('/<int:pk>/delete/', rest_delete, name='rest_delete'),
    ]