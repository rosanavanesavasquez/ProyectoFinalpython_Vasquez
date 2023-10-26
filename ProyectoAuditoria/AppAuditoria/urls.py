from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_de_inicio, name='pagina_de_inicio'),
    path('auditores/', views.listar_auditores, name='lista_auditores'),
    path('auditados/', views.lista_auditados, name='lista_auditados'),
    path('sectores/', views.lista_sectores, name='lista_sectores'),
    path('entregables/', views.lista_entregables, name='lista_entregables'),
    path('entregablesFormulario/', views.entregables_Formulario, name="entregables_Formulario"),
    path('leerEntregables', views.leerEntregables, name="LeerEntregables"),
    path('auditorFormulario/', views.auditorFormulario, name='auditorFormulario'),
    path('busquedaAuditor/', views.busquedaAuditor, name= "BusquedaAuditor"),
    path('buscar/', views.buscar),
    path('agregar_sector/', views.agregar_sector, name='agregar_sector'),
]
