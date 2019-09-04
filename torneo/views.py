from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse
import django


# Create your views here.
from django.shortcuts import get_object_or_404, render
from .models import Capitan,Integrante,Fase,Torneo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from torneo.registroForm import RegistroForm,RegistroIntegrante,FinalizarTorneo
from django.contrib.auth.decorators import login_required
from random import randint
from datetime import datetime as tiempo
from django.core.exceptions import ObjectDoesNotExist


@login_required
def equipoCapitan(request):
    
    if request.user.is_superuser:
        nuevaCadena = nombreTorneo()
        try:
            torneo = Torneo.objects.get(nombre=nuevaCadena)
        except ObjectDoesNotExist:
            torneo = None
        return render(request,'torneo/panelAdministracion.html',{"torneo":torneo})
    else: 
        capitan = get_object_or_404(Capitan, pk=request.user.pk)
        faseDeGrupos = len(Fase.objects.filter(user__exact=capitan,tipoEtapas__exact="Grupo"))
        return render(request,'torneo/equipoCapitan.html',{'capitan':capitan,'fase':faseDeGrupos})
   
def fotos(request):
    return HttpResponse("Estamos en consutruccion")

def historialTorneos(request):
    torneos = Torneo.objects.exclude(fechaFin__isnull=True)

    return render(request,'torneo/historialTorneos.html',{'torneos':torneos})

@login_required
def empezarTorneo(request):
    if request.user.is_staff:
        torneo = Torneo()
        torneo.save()
        return redirect("/torneo/equipo/")
    else:
        return HttpResponse("Ey no puedes hacer eso")

@login_required
def finalizarTorneo(request):
    if not(request.user.is_staff):
        return HttpResponse("Ey no puedes hacer eso")
    nuevaCadena = nombreTorneo()
    try:
        torneo = Torneo.objects.get(nombre=nuevaCadena)
        equiposInscritos = Fase.objects.all().delete()
        
        if request.method == 'POST':
            form = FinalizarTorneo(request.POST,instance=torneo)
            if form.is_valid():
                formulario = form.save(commit=False)
                torneo.fechaFin = django.utils.timezone.now()
                formulario.save()
                return redirect("/torneo/equipo")
        else:
            form = FinalizarTorneo()

        return render(request, 'torneo/finalizarTorneo.html', {'form': form,'torneo':torneo}) 
    except ObjectDoesNotExist:
        return HttpResponse("Estamos en consutruccion")
    

def posiciones(request):
    grupoA = Fase.objects.filter(tipoGrupos__exact="A",tipoEtapas__exact="Grupo")
    grupoB = Fase.objects.filter(tipoGrupos__exact="B",tipoEtapas__exact="Grupo")
    grupoC = Fase.objects.filter(tipoGrupos__exact="C",tipoEtapas__exact="Grupo")
    grupoD = Fase.objects.filter(tipoGrupos__exact="D",tipoEtapas__exact="Grupo")
    grupoE = Fase.objects.filter(tipoGrupos__exact="E",tipoEtapas__exact="Grupo")
    matriz = []
    for i in range(4):
        if i>=len(grupoA):
            A = None
        else:
            A = grupoA[i]
        if i>=len(grupoB):
            B = None
        else:
            B = grupoB[i]
        if i>=len(grupoC):
            C = None
        else:
            C = grupoC[i]
        if i>=len(grupoD):
            D = None
        else:
            D = grupoD[i]
        if i>=len(grupoE):
            E = None
        else:
            E = grupoE[i]
        matriz += [[A,B,C,D,E]]

    return render(request,'torneo/posiciones.html',{'range':range(5),'matriz':matriz})

def contactenos(request):
    return HttpResponse("Estamos en consutruccion")
    
def eliminarIntegrante(request,integrante_id):
    integrante = get_object_or_404(Integrante,pk=integrante_id)
    integrante.delete()
    capitan = get_object_or_404(Capitan, pk=request.user.pk)
    return redirect("/torneo/equipo")

def integranteModificacion(request,integrante_id):
    capitan = get_object_or_404(Capitan, pk=request.user.pk)
    integrante = Integrante.objects.filter(pk=integrante_id)
    if integrante[0].capitan != capitan:
        return HttpResponse("Ey no puedes hacer eso")


    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        integrante = Integrante.objects.filter(capitan=capitan,pk=integrante_id)
        form = RegistroIntegrante(request.POST,instance=integrante[0])
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            formulario = form.save(commit=False)
            formulario.save()
            # redirect to a new URL:
            return redirect("/torneo/equipo")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegistroIntegrante()

    return render(request, 'torneo/modificarIntegrante.html', {'form': form,'integrante':integrante[0]})


@login_required
def inscripcionEquipo(request):
    capitan = get_object_or_404(Capitan, pk=request.user.pk)
    #flag permite comprobar si el usuario puede inscribir el equipo o no.
    flag = True
    try:
        torneo = Torneo.objects.get(nombre=nombreTorneo(),fechaFin=None)
    except ObjectDoesNotExist:
        flag = False
        return HttpResponse("No hay torneo activo, intenta despues")

    if len(Integrante.objects.filter(capitan=request.user))<7 and len(Integrante.objects.filter(capitan=request.user))>10:
        flag = False
        return HttpResponse("Tienes que tener registrados de 7 a 10 integrantes")


    if len(Fase.objects.filter(tipoEtapas__exact="Grupo")) >= 20:
        flag = False
    for i in Fase.objects.all():
        if i.user == capitan:
            flag = False
            break
    grupoA = Fase.objects.filter(tipoGrupos__exact="A",tipoEtapas__exact="Grupo")
    grupoB = Fase.objects.filter(tipoGrupos__exact="B",tipoEtapas__exact="Grupo")
    grupoC = Fase.objects.filter(tipoGrupos__exact="C",tipoEtapas__exact="Grupo")
    grupoD = Fase.objects.filter(tipoGrupos__exact="D",tipoEtapas__exact="Grupo")
    grupoE = Fase.objects.filter(tipoGrupos__exact="E",tipoEtapas__exact="Grupo")
    tipos = [(grupoA,"A"),(grupoB,"B"),(grupoC,"C"),(grupoD,"D"),(grupoE,"E")]
    while flag:
        actual = tipos[randint(0,4)]
        if 0<=len(actual[0]) and len(actual[0])<5:
            flag = False
            superFase = Fase(user=capitan,tipoEtapas="Grupo",tipoGrupos=actual[1])
            superFase.save()
    return redirect("/torneo/equipo")

 


def home(request):
    return render(request,'torneo/index.html')

@login_required
def registroIntegrante(request):
    capitan = get_object_or_404(Capitan, pk=request.user.pk)
    integrantes = Integrante.objects.filter(capitan=capitan)
    if len(integrantes) == 10:
        #Colocar un render a un error de que ya tiene 11 miembros en su equipo
        return render(request,'torneo/equipoCapitan.html',{'capitan':capitan})

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegistroIntegrante(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            formulario = form.save(commit=False)
            capitan = get_object_or_404(Capitan, pk=request.user.pk)
            formulario.capitan = capitan
            formulario.save()
            # redirect to a new URL:
            return redirect("/torneo/equipo")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegistroIntegrante()

    return render(request, 'torneo/registroIntegrante.html', {'form': form})
    
class RegistroUsuario(CreateView):
    model = Capitan
    template_name = "torneo/registrar.html"
    form_class = RegistroForm
    success_url = "/torneo"

def nombreTorneo():
    tiempoActual = tiempo.now()
    if tiempoActual.month <5:
        semestre = 1
    elif tiempoActual.month > 7:
        semestre = 2
    else:
        semestre = "I"
    nuevaCadena = str(tiempoActual.year)+"-"+str(semestre)
    return nuevaCadena
