from django.contrib import admin
from cuentas import models
# Register your models here.

class LocalidadAdmin(admin.ModelAdmin):
	ordering = ('nombre',)

class CuentaAdmin(admin.ModelAdmin):
	list_filter = ('localidad',)

class MovimientoAdmin(admin.ModelAdmin):
	date_hierarchy = 'fecha'
	list_filter = ('cuenta__nombre',)

class PerfilEmpleadoAdmin(admin.ModelAdmin):
	pass

class GerenteDeCuentasAdmin(admin.ModelAdmin):
	pass

admin.site.register(models.Localidad, LocalidadAdmin)
admin.site.register(models.Cuenta, CuentaAdmin)
admin.site.register(models.Movimiento, MovimientoAdmin)
admin.site.register(models.PerfilEmpleado, PerfilEmpleadoAdmin)
admin.site.register(models.GerenteDeCuentas, GerenteDeCuentasAdmin)