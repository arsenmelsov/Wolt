from django.urls import path
from .views import courier_list, courier_detail, courier_new, courier_edit, courier_delete

urlpatterns = [
    path('couriers/', courier_list, name='courier_list'),
    path('courier/<int:pk>/', courier_detail, name='courier_detail'),
    path('courier/new/', courier_new, name='courier_new'),
    path('courier/<int:pk>/edit/', courier_edit, name='courier_edit'),
    path('courier/<int:pk>/delete/', courier_delete, name='courier_delete'),
    ]