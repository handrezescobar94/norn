from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def inicio_page(request):
    return render(request, 'usuario/inicio.html')

def login_page(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user  = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            messages.warning(request, 'El usuario o contraseña son incorrectos.')
    return render(request, 'auth/login.html')

def logout_user(request):
    logout(request)
    return redirect('login')