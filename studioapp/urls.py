from django.urls import path
from . import views

from .views import Custom_login, home
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name='home'),
    path('work/', views.work, name='work'),
    path('services/', views.service, name='services'),
    path('contact/', views.contact, name='contact'),
    path('booking_list/',views.booking_list, name='bookinglog'),
    path('login/', Custom_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('signup/', views.signup_view, name='signup'), 
   
]


