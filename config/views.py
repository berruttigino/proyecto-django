from django.shortcuts import render

def saludo(request):
    contexto = {'usuario': 'Gino'}
    return render(request, 'saludo.html', contexto)