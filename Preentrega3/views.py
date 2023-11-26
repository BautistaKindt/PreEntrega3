from django.http import HttpResponse
from django.shortcuts import render


def saludo(request):
    contexto = {}
    return render(request, 'index.html', contexto)
