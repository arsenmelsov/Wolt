from django.urls import path
from .views import houseType_list, houseType_detail, houseType_new, houseType_edit, houseType_delete

urlpatterns = [
    path('', houseType_list, name='houseType_list'),
    path('/<int:pk>/', houseType_detail, name='houseType_detail'),
    path('/new/', houseType_new, name='houseType_new'),
    path('/<int:pk>/edit/', houseType_edit, name='houseType_edit'),
    path('/<int:pk>/delete/', houseType_delete, name='houseType_delete'),
    ]