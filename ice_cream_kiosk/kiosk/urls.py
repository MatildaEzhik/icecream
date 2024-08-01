from django.urls import path
from django.contrib.auth import views as auth_views

from kiosk.views import ice_cream_list, kiosk_list, ice_cream_search, signup, user_profile

urlpatterns = [
    path('', kiosk_list, name='kiosk_list'),
    path('ice_creams/', ice_cream_list, name='ice_cream_list'),
    path('search/', ice_cream_search, name='ice_cream_search'),
    path('signup/', signup, name='signup'),
    path('profile/', user_profile, name='user_profile'),
    path('login/', auth_views.LoginView.as_view(template_name='kiosk/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]

