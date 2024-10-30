from django.contrib import admin
from aplication.core.models import (
    MarcaMedicamento, TipoSangre, Paciente, Especialidad, Doctor, Cargo, Empleado, TipoMedicamento, 
    Medicamento, Diagnostico, CategoriaExamen, TipoCategoria
)

# Registro de TipoSangre
@admin.register(TipoSangre)
class TipoSangreAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'descripcion')
    search_fields = ('tipo',)


# Registro de Paciente
@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'cedula', 'fecha_nacimiento', 'sexo', 'estado_civil')
    search_fields = ('nombres', 'apellidos', 'cedula')
    list_filter = ('sexo', 'estado_civil', 'tipo_sangre')
    ordering = ['apellidos']

    

# Registro de Especialidad
@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)


# Registro de Doctor
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'cedula', 'codigoUnicoDoctor')
    search_fields = ('nombres', 'apellidos', 'cedula', 'codigoUnicoDoctor')
    list_filter = ('especialidad',)
    
    def nombre_completo(self, obj):
        return obj.nombre_completo()
    nombre_completo.short_description = "Nombre Completo"


# Registro de Cargo
@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)


# Registro de Empleado
@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'cedula', 'cargo', 'sueldo')
    search_fields = ('nombres', 'apellidos', 'cedula')
    list_filter = ('cargo',)
    
    def nombre_completo(self, obj):
        return obj.nombre_completo()
    nombre_completo.short_description = "Nombre Completo"


# Registro de TipoMedicamento
@admin.register(TipoMedicamento)
class TipoMedicamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)


# Registro de Medicamento
@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'cantidad', 'precio', 'comercial')
    search_fields = ('nombre', 'tipo__nombre')
    list_filter = ('comercial', 'tipo')


# Registro de Diagnostico
@admin.register(Diagnostico)
class DiagnosticoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descripcion')
    search_fields = ('codigo', 'descripcion')

# Registro de Diagnostico
@admin.register(MarcaMedicamento)
class MarcaMedicamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)


# Registro de CategoriaExamen
@admin.register(CategoriaExamen)
class CategoriaExamenAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)


# Registro de TipoCategoria
@admin.register(TipoCategoria)
class TipoCategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria_examen')
    search_fields = ('nombre', 'categoria_examen__nombre')
    list_filter = ('categoria_examen',)

