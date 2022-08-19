from django.shortcuts import render

def principal(request):
    return render(request, 'inicio/principal.html')

def contacto(request):
    return render(request, 'inicio/contacto.html')

def pendientes(request):
    return render(request, 'inicio/pendientes.html')

def ninos(request):
    return render(request, 'inicio/ninos.html')

def entregables(request):
    return render(request, 'inicio/entregables.html')