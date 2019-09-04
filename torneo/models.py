from django.db import models
from django import forms
from django.contrib.auth.models import User
from datetime import datetime as tiempo

# Create your models here.


class Capitan(User):
    user = models.OneToOneField(User,on_delete=models.CASCADE,parent_link=True)
    tDocumentos = (("CC","Cedula Ciudadania"),("TI","Tarjeta Identidad"),("CE","Cedula Extranjeria"))
    tipoDocumento = models.CharField(max_length=2,choices=tDocumentos,default="CC")
    numeroDocumento = models.CharField(max_length=11,unique=True)
    carne = models.CharField(max_length=7,unique=True)
    tAfinacion = (("Pregrado","Pregrado"),("Posgrado","Posgrado"),("Graduado","Graduado"),("Profesor","Profesor"),("Personal Administrativo","Personal Administrativo"))
    afinacion = models.CharField(max_length=23,choices=tAfinacion,default="Pregrado")
    celular = models.CharField(max_length=10)
    semestre = models.CharField(max_length=2,null = True,blank=True) #solo es requerido si es pregrado
    semestreGrado = models.CharField(max_length=6,null = True,blank=True) #Para graduados EJ: 2019-2
    nombreEquipo = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return self.user.username+" - "+ self.first_name +" "+ self.last_name+" - "+ self.nombreEquipo

class Integrante(models.Model):
    capitan = models.ForeignKey(Capitan, on_delete= models.CASCADE)
    nombreCompleto = models.CharField(max_length=200)
    apellidoCompleto = models.CharField(max_length=200)
    semestre = models.CharField(max_length=2,null=True,blank=True)
    carne = models.CharField(max_length=7,unique=True,blank=True)
    
    def __str__(self):
        return self.nombreCompleto+" "+self.apellidoCompleto
    
class Fase(models.Model):
    user = models.ForeignKey(Capitan, on_delete= models.CASCADE)
    tEtapas = (("Grupo","Grupo"),("Cuartos","Cuartos de Final"),("Semifinal","Semifinal"),("Final","Final"))
    tipoEtapas = models.CharField(max_length=10,choices=tEtapas,default="Grupo")
    tGrupos = (("A","A"),("B","B"),("C","C"),("D","D"),("E","E"))
    tipoGrupos = models.CharField(max_length=1,choices=tGrupos,default="A",null=True,blank=True)

    def __str__(self):
        return self.user.nombreEquipo+" - "+self.tipoEtapas

class Torneo(models.Model):
    tiempoActual = tiempo.now()
    if tiempoActual.month <5:
        semestre = 1
    elif tiempoActual.month > 7:
        semestre = 2
    else:
        semestre = "I"
    nuevaCadena = str(tiempoActual.year)+"-"+str(semestre)
    nombre = models.CharField(max_length=6,default=nuevaCadena,editable=False,unique=True)
    fechaInicio = models.DateField(auto_now_add=True,editable=False)
    fechaFin = models.DateField(null=True,blank=True)
    primerPuesto = models.ForeignKey(Capitan, on_delete= models.CASCADE,related_name='primerPuesto',null=True,blank=True)
    segundoPuesto = models.ForeignKey(Capitan, on_delete= models.CASCADE,related_name='segundoPuesto',null=True,blank=True)
    tercerPuesto = models.ForeignKey(Capitan, on_delete= models.CASCADE,related_name='tercerPuesto',null=True,blank=True)


    def __str__(self):
        return self.nombre
