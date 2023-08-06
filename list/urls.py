from django.urls import path
from . import views

urlpatterns = [
    path('', views.listing_list, name='listing-list'),
    path('listings/create/', views.listing_create, name='listing-create'),
    path('listings/<int:pk>/', views.listing_detail, name='listing-detail'),
    path('listings/<int:pk>/update/', views.listing_update, name='listing-update'),
    path('listings/<int:pk>/delete/', views.listing_delete, name='listing-delete'),
]
