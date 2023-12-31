from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

#Para el login
from django.contrib.auth.decorators import login_required

#Para el logout
from django.contrib.auth.views import LogoutView

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
    #path('delete-sector/<str:sector_nombre>/', views.delete_sector, name='DeleteSector'),    
    path('delete-sector/<int:sector_id>/',views.delete_sector,name='DeleteSector'),
    #path('edit-sector/<int:sector_id>/',views.edit_sector,name='EditSector'),    
    
    path('sector/list', views.SectorList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.SectorDetalle.as_view(), name='Detail'),
    path(r'^nuevo$',views.SectorCreacion.as_view(),name='New'),
    path(r'editar/(?P<pk>\d+)$', views.SectorUpdate.as_view(), name='Edit'),
    path(r'borrar/(?P<pk>\d+)$', views.SectorDelete.as_view(), name='Delete'),    
    
    #para Usuarios
    path('login', views.login_request, name="Login"),
    path('register', views.register, name = 'Register'),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name = 'Logout'),

    #path('editarPerfil', views.editarPerfil, name="EditarPerfil"),

    #path('agregarAvatar', views.agregarAvatar, name="AgregarAvatar"),
] 
