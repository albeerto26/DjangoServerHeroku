from django.contrib import admin

# Register your models here.
from .models import *


class TraperoAdmin(admin.ModelAdmin):
    list_display = ('aka', 'nombre_real', 'ano_nacimiento', 'foto', 'edad', )
    list_filter = ('aka', 'nombre_real', 'ano_nacimiento', 'foto', )
    search_fields = ('aka', 'nombre_real')


class DiscoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_publicacion', 'portada', 'trapero', )
    list_filter = ('nombre', 'fecha_publicacion', 'portada', 'trapero', )
    search_fields = ('nombre', 'trapero__aka')


class TiraeraAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_inicio', 'descripcion', 'trapero_tira', 'trapero_recibe')
    list_filter = ('titulo', 'fecha_inicio', 'descripcion', 'trapero_tira', 'trapero_recibe')
    search_fields = ('titulo', 'trapero_tira__aka', 'trapero_tira__aka')


class AlertaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_alerta', 'trapero')
    list_filter = ('titulo', 'fecha_alerta', 'trapero')
    search_fields = ('titulo', 'trapero__aka', )


admin.site.register(Trapero, TraperoAdmin)
admin.site.register(Disco, DiscoAdmin)
admin.site.register(Tiraera, TiraeraAdmin)
admin.site.register(Alerta, AlertaAdmin)
