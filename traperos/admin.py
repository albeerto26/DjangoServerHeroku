"""Import del modulo de gestion de admin."""
from django.contrib import admin

# Register your models here.
from .models import Trapero, Disco, Tiraera, Alerta


class TraperoAdmin(admin.ModelAdmin):
    """Definicion de panel admin para modulo Trapero."""

    list_display = ('aka', 'nombre_real', 'ano_nacimiento', 'foto', 'edad', )
    list_filter = ('aka', 'nombre_real', 'ano_nacimiento', 'foto', )
    search_fields = ('aka', 'nombre_real')


class DiscoAdmin(admin.ModelAdmin):
    """Definicion de panel admin para modulo Disco."""

    list_display = ('nombre', 'fecha_publicacion', 'portada', )
    list_filter = ('nombre', 'fecha_publicacion', 'portada', )
    search_fields = ('nombre', 'trapero__aka')


class TiraeraAdmin(admin.ModelAdmin):
    """Definicion de panel admin para modulo Tiraera."""

    list_display = ('titulo', 'fecha_inicio', 'descripcion', 'trapero_tira', 'trapero_recibe')
    list_filter = ('titulo', 'fecha_inicio', 'descripcion', 'trapero_tira', 'trapero_recibe')
    search_fields = ('titulo', 'trapero_tira__aka', 'trapero_tira__aka')


class AlertaAdmin(admin.ModelAdmin):
    """Definicion de panel admin para modulo Alerta."""

    list_display = ('titulo', 'fecha_alerta', 'trapero')
    list_filter = ('titulo', 'fecha_alerta', 'trapero')
    search_fields = ('titulo', 'trapero__aka', )


admin.site.register(Trapero, TraperoAdmin)
admin.site.register(Disco, DiscoAdmin)
admin.site.register(Tiraera, TiraeraAdmin)
admin.site.register(Alerta, AlertaAdmin)
