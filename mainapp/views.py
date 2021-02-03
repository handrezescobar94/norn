from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.serializers import serialize

from .models import LoginLog

import datetime

# Create your views here.
def index_page(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        return redirect('login')

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
            log = LoginLog.objects.create(user = user)
            return redirect('inicio')
        else:
            messages.warning(request, 'El usuario o contraseña son incorrectos.')
    return render(request, 'auth/login.html')

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def login_logs(request):
    return render(request, 'usuario/login-log.html')

@login_required(login_url='login')
def filter_login_logs(request):
    rango = request.GET.get('filter_date')
    fechas = rango.split(' - ')
    fecha_inicio = datetime.datetime.strptime(fechas[0], "%Y-%m-%d %H:%M:%S")
    fecha_fin = datetime.datetime.strptime(fechas[1], "%Y-%m-%d %H:%M:%S")
    logs = LoginLog.objects.filter(created_at__range=(fecha_inicio, fecha_fin))
    html = render(request, 'usuario/login-log-rows.html', {"logs": logs})
    return HttpResponse(html)