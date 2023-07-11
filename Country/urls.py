from django.urls import path
from .views import country_list, country_detail, country_new, country_edit, country_delete

urlpatterns = [
    path('countrys/', country_list, name='country_list'),
    path('country/<int:pk>/', country_detail, name='country_detail'),
    path('country/new/', country_new, name='country_new'),
    path('country/<int:pk>/edit/', country_edit, name='country_edit'),
    path('country/<int:pk>/delete/', country_delete, name='country_delete'),
    ]