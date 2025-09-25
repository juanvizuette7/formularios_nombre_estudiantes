from django.contrib import admin
from .models import Asistencia

# Register your models here.

@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'documento_identidad', 'fecha_asistencia', 'hora_ingreso', 'hora_salida', 'presente')
    list_filter = ('fecha_asistencia', 'presente')
    search_fields = ('nombre_completo', 'documento_identidad', 'correo_electronico')
    date_hierarchy = 'fecha_asistencia'
    ordering = ('-fecha_asistencia', '-hora_ingreso')
    
    fieldsets = (
        ('Información Personal', {
            'fields': ('nombre_completo', 'documento_identidad', 'correo_electronico')
        }),
        ('Información de Asistencia', {
            'fields': ('fecha_asistencia', 'hora_ingreso', 'hora_salida', 'presente')
        }),
        ('Observaciones', {
            'fields': ('observaciones',),
            'classes': ('collapse',)
        }),
    )
