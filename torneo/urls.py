from django.urls import path

from . import views

app_name = "torneo"

urlpatterns = [

    path('equipo/',views.equipoCapitan,name='mostrarEquipo'),
    path('',views.home,name='home'),
    path('fotos',views.fotos,name="fotos"),
    path('posiciones/',views.posiciones,name="posiciones"),
    path('equipo/<int:integrante_id>/',views.integranteModificacion,name="ModificiacionIntegrante"),
    path('equipo/registroIntegrante',views.registroIntegrante,name="registroIntegrante"),
    path('inscripcion',views.inscripcionEquipo,name="InscripcionEquipo"),
    path('contactenos',views.contactenos,name="contactenos"),
    path('posiciones/historialTorneos',views.historialTorneos,name="historialTorneos"),
    #TERMINAR VER TABLERO
    path('equipo/empezarTorneo',views.empezarTorneo,name="empezarTorneo"),
    #TERMINAR VER TABLERO
    path('equipo/finalizarTorneo',views.finalizarTorneo,name="finalizarTorneo"),
    path('equipo/<int:integrante_id>/eliminar',views.eliminarIntegrante,name="EliminarIntegrante"),
    #path('<int:capitan_id>/',views.equipoCapitan,name='mostrarEquipo'),
    #path('<int:capitan_id>/',views.equipoCapitan,name='mostrarEquipo'),
    #path('',None,name='mostrarCaracteristicas'),
    #path('',None,name='inscribete'),
    #path('',None,name='configuraEquipo'),

]
