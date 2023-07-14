from django.urls import path
from .views import branch_list, branch_detail, branch_new, branch_edit, branch_delete

urlpatterns = [
    path('', branch_list, name='branch_list'),
    path('/<int:pk>/', branch_detail, name='branch_detail'),
    path('/new/', branch_new, name='branch_new'),
    path('/<int:pk>/edit/', branch_edit, name='branch_edit'),
    path('/<int:pk>/delete/', branch_delete, name='branch_delete'),
    ]