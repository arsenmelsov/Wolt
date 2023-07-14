from django.urls import path
from .views import category_list, category_detail, category_new, category_edit, category_delete

urlpatterns = [
    path('/', category_list, name='category_list'),
    path('/<int:pk>/', category_detail, name='category_detail'),
    path('/new/', category_new, name='category_new'),
    path('/<int:pk>/edit/', category_edit, name='category_edit'),
    path('/<int:pk>/delete/', category_delete, name='category_delete'),
    ]