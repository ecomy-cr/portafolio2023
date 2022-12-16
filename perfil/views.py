from django.shortcuts import render, redirect

def perfil(request):
    return render(request, "perfil.html")

def portafolio(request):
    return render(request, "portafolio.html")
