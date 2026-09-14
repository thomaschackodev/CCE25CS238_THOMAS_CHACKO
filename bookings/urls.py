from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('bookings/', views.booking_list, name='booking_list'),
    path('bookings/add/', views.booking_add, name='booking_add'),
    path('bookings/edit/<int:pk>/', views.booking_edit, name='booking_edit'),
    path('bookings/delete/<int:pk>/', views.booking_delete, name='booking_delete'),
]
