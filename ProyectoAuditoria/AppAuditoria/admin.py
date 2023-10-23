from django.contrib import admin
from.models import *

# Acá registro los modelos y los tengo que importar para que los pueda usar. 
# #Importo todo * pero podría seleccionar solo el modelo que quiero

admin.site.register(Auditor)
admin.site.register(Auditado)
admin.site.register(Sector)
admin.site.register(Entregable)

