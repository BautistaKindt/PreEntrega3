from django.shortcuts import render
from django.http import HttpResponse
from Entrega3CoderApp.models import Alumno
from Entrega3CoderApp.forms import Alumno_Formulario


def mostrar_alumnos(request):
    alumno = Alumno.objects.all()
    contexto = {
        "alumno": alumno
    }
    return render(request, "alumnos.html", contexto)

def alumno_formulario(request):
    if request.method == 'POST':
        miformulario = Alumno_Formulario(request.POST)
        print(miformulario)
        if miformulario.is_valid():
            informacion = miformulario.cleaned_data
            alumno = Alumno(nombre=informacion['alumno'], legajo=informacion['legajo'])
            alumno.save()
            return render(request, 'padre.html')
    else:
        miformulario = Alumno_Formulario()
    return render(request, "alumno_formulario.html", {"miformulario": miformulario})


def buscar_legajo(request):
    return render(request, 'buscar_legajo.html')

def buscar(request):
    respuesta = f"Buscando alumno con legajo: {request.GET['legajo']}"
    return HttpResponse(respuesta)