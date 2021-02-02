from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def holaMundo(request):
    return render(request, 'holaMundo.html')

def pagina(request):
    year = 2021
    year_limit = 2051
    rango = range(year, year_limit)
    return render(request, 'pagina.html', {
        'year_limit': year_limit-1,
        'rango': rango
    })

def contacto(request, nombre = "No Asignado"):
    lenguajes = [
        'PHP',
        'CSS',
        'JS',
        'HTML',
        'JS',
        'PYTHON'
    ]
    return render(request, 'contacto.html', {
        'nombre_contacto': nombre,
        'edad': 16,
        'lenguajes': lenguajes
    })