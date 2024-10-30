from django.contrib import admin
from aplication.attention.models import (
    HorarioAtencion,
    CitaMedica,
    Atencion,
    DetalleAtencion,
    ExamenSolicitado,
    ServiciosAdicionales,
    CostosAtencion,
)

# Admin para HorarioAtencion
@admin.register(HorarioAtencion)
class HorarioAtencionAdmin(admin.ModelAdmin):
    list_display = ('dia_semana', 'hora_inicio', 'hora_fin')
    search_fields = ('dia_semana',)

# Admin para CitaMedica
@admin.register(CitaMedica)
class CitaMedicaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'fecha', 'hora_cita', 'estado')
    list_filter = ('estado', 'fecha')
    search_fields = ('paciente__nombre',)

# Admin para DetalleAtencion
class DetalleAtencionInline(admin.TabularInline):
    model = DetalleAtencion
    extra = 1  # Número de formularios vacíos a mostrar

# Admin para Atencion
@admin.register(Atencion)
class AtencionAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'fecha_atencion', 'motivo_consulta')
    search_fields = ('paciente__nombre',)
    inlines = [DetalleAtencionInline]  # Configura DetalleAtencion como inline

# Admin para DetalleAtencion
@admin.register(DetalleAtencion)
class DetalleAtencionAdmin(admin.ModelAdmin):
    list_display = ('atencion', 'medicamento', 'cantidad', 'prescripcion')
    search_fields = ('atencion__paciente__nombre', 'medicamento__nombre')

# Admin para ExamenSolicitado
@admin.register(ExamenSolicitado)
class ExamenSolicitadoAdmin(admin.ModelAdmin):
    list_display = ('nombre_examen', 'paciente', 'fecha_solicitud', 'estado')
    search_fields = ('nombre_examen', 'paciente__nombre')

# Admin para ServiciosAdicionales
@admin.register(ServiciosAdicionales)
class ServiciosAdicionalesAdmin(admin.ModelAdmin):
    list_display = ('nombre_servicio', 'costo_servicio')
    search_fields = ('nombre_servicio',)

# Admin para CostosAtencion
@admin.register(CostosAtencion)
class CostosAtencionAdmin(admin.ModelAdmin):
    list_display = ('atencion', 'total', 'fecha_registro')
    search_fields = ('atencion__paciente__nombre',)


