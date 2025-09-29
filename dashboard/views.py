from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login_view(request):
     if request.user.is_authenticated:
          
          return redirect('dashboard-home')
    
     if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # checkout username and password
        user = authenticate(request,username=username,password=password)

        if user:
            login(request=request, user=user)
            return redirect('dashboard-home')
        else:
             messages.error(request, 'Invalid username or password')

     return render(request, 'dashboard/login.html')

@login_required
def dashboard_home(request):
    return render(request, 'dashboard/index.html')

def logout_view(request):
    logout(request)
    return redirect('login')
