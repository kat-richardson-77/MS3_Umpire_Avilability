from django.urls import path
from .views import indexpageview, adduserpageview

urlpatterns = [
    path('', indexpageview, name='index'),
    path('adduser/', adduserpageview, name='adduser'), 
]