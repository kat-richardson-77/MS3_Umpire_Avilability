from django.shortcuts import render 
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import User
from django.http import HttpResponse
from .forms import UserRegisterForm

def indexpageview(request):
    return render(request, 'home.html')

def adduserpageview(request):
    return render(request, 'adduser.html')

def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            message = f'User {username} registered successfully!'
            return redirect('login')  # Redirect to the login page after successful registration

    else:
        form = UserRegisterForm()
    return render(request, 'requestumpire.html')

@login_required
def home(request):
    return render(request, 'requestumpire.html')