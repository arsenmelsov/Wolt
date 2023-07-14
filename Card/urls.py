from django.urls import path
from .views import card_list, card_detail, card_new, card_edit, card_delete

urlpatterns = [
    path('/', card_list, name='card_list'),
    path('/<int:pk>/', card_detail, name='card_detail'),
    path('/new/', card_new, name='card_new'),
    path('/<int:pk>/edit/', card_edit, name='card_edit'),
    path('/<int:pk>/delete/', card_delete, name='card_delete'),
    ]