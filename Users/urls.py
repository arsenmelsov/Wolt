from django.urls import path
from .views import*

urlpatterns = [
    path('', user_list, name='user_list'),
    path('<int:pk>/', user_detail, name='user_detail'),
    path('new/', user_new, name='user_new'),
    path('<int:pk>/edit/', user_edit, name='user_edit'),
    path('<int:pk>/delete/', user_delete, name='user_delete'),
    path('register/', user_register, name='user_register'),
    path('login/', user_login, name='login'),
    ]