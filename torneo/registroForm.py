from django.contrib.auth.models import User
from django import forms
from .models import Capitan,Integrante,Torneo
from django.contrib.auth.forms import UserCreationForm


class RegistroForm(UserCreationForm):
    class Meta:
        model = Capitan
        fields = [
                'username',
                'first_name',
                'last_name',
                'email',
                'tipoDocumento',
                'numeroDocumento',
                'carne',
                'afinacion',
                'celular',
                'semestre',
                'semestreGrado',
                'nombreEquipo',

            ]

class RegistroIntegrante(forms.ModelForm):
    class Meta:
        model = Integrante
        fields = [
                'nombreCompleto',
                'apellidoCompleto',
                'semestre',
                'carne',
            ]
class ModificacionIntegrante(forms.ModelForm):
    class Meta:
        model = Integrante
        fields = [
                'nombreCompleto',
                'apellidoCompleto',
                'semestre',
                'carne',
            ]

class FinalizarTorneo(forms.ModelForm):
    class Meta:
        model = Torneo
        fields = [
                'primerPuesto',
                'segundoPuesto',
                'tercerPuesto',
            ]



