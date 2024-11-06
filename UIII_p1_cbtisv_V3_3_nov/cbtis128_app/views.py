from django.shortcuts import render,redirect
from .models import Materia
from django.contrib import messages
# Create your views here.

def inicio_vista(request):
    lasmaterias=Materia.objects.all()
    messages.success(request, '¡Materias Listadas!')
    return render(request,'gestionarMateria.html',{'mismaterias':lasmaterias})

def registrarMateria(request):
    codigo=request.POST['txtcodigo']
    nombre=request.POST['txtnombre']
    creditos=request.POST['numcreditos']
    guardamateria=Materia.objects.create(codigo=codigo,nombre=nombre,creditos=creditos)
    return redirect('/')

def seleccionaMateria(request,codigo):
    materia=Materia.objects.get(codigo=codigo)
    return render(request,"editarmateria.html",{"mismaterias":materia})

def editarMateria(request):
    codigo = request.POST['txtcodigo']
    nombre = request.POST['txtnombre']
    creditos = request.POST['numcreditos']
    materia = Materia.objects.get(codigo=codigo)
    materia.nombre = nombre
    materia.creditos = creditos
    materia.save()

    messages.success(request, '¡Materia actualizada!')

    return redirect('/')

def borrarMateria(request, codigo):
    materia = Materia.objects.get(codigo=codigo)
    materia.delete()

    messages.success(request, '¡Materia eliminada!')

    return redirect('/')
