from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Auditor, Auditado, Sector, Entregable
from AppAuditoria.forms import AuditorFormulario, SectorForm

def pagina_de_inicio(request):
    return render(request, 'AppAuditoria/index.html')

def listar_auditores(request):
    auditores = Auditor.objects.all()
    return render(request, 'appauditoria/lista_auditores.html', {'auditores': auditores})

def lista_auditados(request):
    auditados = Auditado.objects.all()
    return render(request, 'appauditoria/lista_auditados.html', {'auditados': auditados})

def lista_sectores(request):
    sectores = Sector.objects.all()
    return render(request, 'appauditoria/lista_sectores.html', {'sectores': sectores})

def lista_entregables(request):
    entregables = Entregable.objects.all()
    return render(request, 'appauditoria/lista_entregables.html', {'entregables': entregables})

def entregables_Formulario(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        fecha_de_auditoria = request.POST['fechaDeAuditoria']
        resultado_auditoria = request.POST['resultado_auditoria']

        # Crea una nueva instancia de Entregable y la guardará en la base de datos
        entregable = Entregable(nombre=nombre, fechaDeAuditoria=fecha_de_auditoria)

        if resultado_auditoria == "OK":
            entregable.auditoria_ok = True
        elif resultado_auditoria == "NG":
            entregable.auditoria_ng = True

        entregable.save()

    return render(request, "appauditoria/entregables_Formulario.html")

def leerEntregables(request):

      entregables = Entregable.objects.all() #trae todos los resultados de las auditorias

      contexto= {"entregables":entregables} 

      return render(request, "AppAuditoria/leerEntregables.html",contexto)

def auditorFormulario(request):
    if request.method == "POST":
        miFormulario = AuditorFormulario (request.POST)  # Pasa 'request' como argumento al formulario
        print(miFormulario)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            auditor = Auditor(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"])
            auditor.save()
            return render(request, "AppAuditoria/index.html")  # Redirige 
    else:
        miFormulario = AuditorFormulario()  # 

    return render(request, "AppAuditoria/auditores_Formulario.html",{"miFormulario": miFormulario})  # 

def busquedaAuditor(request):
    return render(request, "AppAuditoria/busquedaAuditor.html")

def buscar(request):
    nombre = request.GET.get('nombre')
    resultados = Auditor.objects.filter(nombre__icontains=nombre)
    contexto = {'resultados': resultados}
    return render(request, 'AppAuditoria/busquedaAuditor.html', contexto)

def agregar_sector(request):
    if request.method == 'POST':
        form = SectorForm(request.POST)
        if form.is_valid():
                  
            nuevo_sector = Sector(
                nombre=form.cleaned_data['nombre'],
                UAP=form.cleaned_data['UAP'],
                UAT=form.cleaned_data['UAT']
            )

            nuevo_sector.save()
            return redirect('lista_sectores')
    else:
        form = SectorForm()
    return render(request, 'appauditoria/agregar_sector.html', {'form': form})

#def delete_sector(request, sector_nombre):
#    print(type(sector_nombre))
#    sector = Sector.objects.get(nombre=sector_nombre)
#    sector.delete()
#    #vuelvo al menu
#    sector = Sector.objects.all()
#    contexto = {"sector": sector}
#    return render(request,"AppAuditoria/lista_sectores.html", contexto)

def delete_sector(request, sector_id):
    print(type(sector_id))
    sector= Sector.objects.get(id=sector_id)
    sector.delete()
    sectores = Sector.objects.all()
    return render(request, 'appauditoria/lista_sectores.html', {'sectores': sectores})
     

 
    
    