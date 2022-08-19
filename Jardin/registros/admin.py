from typing import Sequence
from django.contrib import admin

from .models import Contacto, Tareas, ZonaNiños
from .models import Entregables

# Register your models here.

class AdministartModelo(admin.ModelAdmin):
    readonly_fields: Sequence[str] = ('created', 'update')
    list_display = ('nomTarea', 'clave', 'descripcion', 'FechaEntrega' ,'created', 'update')
    list_filter = ( 'clave', 'descripcion', 'FechaEntrega')
    search_fields = ('nomTarea', 'clave', 'descripcion', 'FechaEntrega')
    ordering = ('created',)
    date_hierarchy = 'created'
    list_per_page = 2
    list_display_links = ('nomTarea', 'descripcion', 'clave')
    list_editable = ['FechaEntrega']
    
admin.site.register(Tareas, AdministartModelo)

class AdministrarEntregables(admin.ModelAdmin):
    readonly_fields: Sequence[str] = ('created', 'update')
    list_display = ('nombreAlumno', 'grupo')
    search_fields: Sequence[str] = ('nombreAlumno', 'grupo')
    date_hierarchy = 'created'
    ordering = ('created',)
    list_editable: Sequence[str] = ('grupo',)

admin.site.register(Entregables, AdministrarEntregables)

class AdministrarContacto(admin.ModelAdmin):
    readonly_fields: Sequence[str] = ('created', 'update')
    list_display = ('nombreP', 'nombreA')
    search_fields: Sequence[str] = ('nombreP', 'nombreA')
    date_hierarchy = 'created'

admin.site.register(Contacto, AdministrarContacto)

class AdministrarVideo(admin.ModelAdmin):
    readonly_fields: Sequence[str] = ('created', 'update')
    list_display = ('nombre', 'enlace')
    date_hierarchy = 'created'

admin.site.register(ZonaNiños, AdministrarVideo)