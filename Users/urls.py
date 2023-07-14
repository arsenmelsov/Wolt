from django.urls import path
from .views import user_list, user_detail, user_new, user_edit, user_delete

urlpatterns = [
    path('', user_list, name='user_list'),
    path('/<int:pk>/', user_detail, name='user_detail'),
    path('/new/', user_new, name='user_new'),
    path('/<int:pk>/edit/', user_edit, name='user_edit'),
    path('/<int:pk>/delete/', user_delete, name='user_delete'),
    ]