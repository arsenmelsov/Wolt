from django.urls import path
from .views import branchAddress_list, branchAddress_detail, branchAddress_new, branchAddress_edit, branchAddress_delete

urlpatterns = [
    path('', branchAddress_list, name='branchAddress_list'),
    path('/<int:pk>/', branchAddress_detail, name='branchAddress_detail'),
    path('/new/', branchAddress_new, name='branchAddress_new'),
    path('/<int:pk>/edit/', branchAddress_edit, name='branchAddress_edit'),
    path('/<int:pk>/delete/', branchAddress_delete, name='branchAddress_delete'),
    ]