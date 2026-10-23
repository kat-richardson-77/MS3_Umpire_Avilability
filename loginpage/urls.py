from turtle import home

from django.contrib import admin
from django.urls import path
from loginpage import views as login_views
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from .views import indexpageview, adduserpageview


def redirect_to_home(request):
    return redirect('index')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('requestumpire/', login_views.home(template_name='requestumpire'), name='requestumpire'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', login_views.register_user, name='register'),
    path('', home, name='home'),
    path('adduser/', adduserpageview, name='adduser'), 
    path('loginpage/' include('loginpage.urls')),  # Include the loginpage app's URLs
]