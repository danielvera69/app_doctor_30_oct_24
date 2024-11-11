from django.db import models
from aplication.core.models import *
from doctor.const import CITA_CHOICES, DIA_SEMANA_CHOICES, EXAMEN_CHOICES

# Modelo que representa los días y horas de atención de un doctor.
# Incluye los días de la semana, la hora de inicio y la hora de fin de la atención.
class HorarioAtencion(models.Model):
    # Días de la semana en los que el doctor atiende
    dia_semana = models.CharField(max_length=10, choices=DIA_SEMANA_CHOICES, verbose_name="Día de la Semana",unique=True)
    # Hora de inicio de atención del doctor
    hora_inicio = models.TimeField(verbose_name="Hora de Inicio")
    # Hora de fin de atención del doctor
    hora_fin = models.TimeField(verbose_name="Hora de Fin")
    # Inicio de descanso de atención del doctor
    Intervalo_desde=models.TimeField(verbose_name="Intervalo desde")
     # Fin de descanso de atención del doctor
    Intervalo_hasta=models.TimeField(verbose_name="Intervalo Hasta")

    activo = models.BooleanField(default=True,verbose_name="Activo")
    
    def __str__(self):
        return f"{self.dia_semana}"

    class Meta:
        # Nombre singular y plural del modelo en la interfaz administrativa
        verbose_name = "Horario de Atenciónl Doctor"
        verbose_name_plural = "Horarios de Atención de los Doctores"

# modelo que almacena los datos de la cita de los pacientes
class CitaMedica(models.Model):
 
     # Relación con el modelo Paciente, indica qué paciente ha reservado la cita
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name="Paciente",related_name="pacientes_citas")
     # Fecha de la cita médica
    fecha = models.DateField(verbose_name="Fecha de la Cita")
    # Hora de la cita médica
    hora_cita = models.TimeField(verbose_name="Hora de la Cita")
    # Estado de la cita (ej. Programada, Cancelada, Realizada)
    estado = models.CharField(
        max_length=1,
        choices=CITA_CHOICES,
        verbose_name="Estado de la Cita"
    )

    def __str__(self):
        return f"Cita {self.paciente} el {self.fecha} a las {self.hora_cita}"

    class Meta:
        # Ordena las citas por fecha y hora
        ordering = ['fecha', 'hora_cita']
        indexes = [
            models.Index(fields=['fecha', 'hora_cita'], name='idx_fecha_hora'),
        ]
        # Nombre singular y plural del modelo en la interfaz administrativa
        verbose_name = "Cita Médica"
        verbose_name_plural = "Citas Médicas"

# Modelo que representa la cabecera de una atención médica.
# Contiene la información general del paciente, diagnóstico, motivo de consulta y tratamiento.
class Atencion(models.Model):
    # Relación con el modelo Paciente, identifica al paciente que recibe la atención médica
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, verbose_name="Paciente",related_name="doctores_atencion")
     # Fecha en la que se realizó la atención médica
    fecha_atencion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Atención")
    # Presión arterial del paciente (ej. "120/80 mmHg")
    presion_arterial = models.CharField(max_length=20, null=True, blank=True, verbose_name="Presión Arterial")
    # Medición del pulso en pulsaciones por minuto
    pulso = models.IntegerField(null=True, blank=True, verbose_name="Pulso (ppm)")
     # Temperatura corporal en grados Celsius
    temperatura = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Temperatura (°C)")
    # Frecuencia respiratoria en respiraciones por minuto
    frecuencia_respiratoria = models.IntegerField(null=True, blank=True, verbose_name="Frecuencia Respiratoria(rpm)")
    # Saturación de oxígeno en sangre (SpO2)
    saturacion_oxigeno = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Saturación de Oxígeno (%)")
    # Peso del paciente en kilogramos
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Peso (kg)")
    # Altura del paciente en metros
    altura = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, verbose_name="Altura (m)")
    # Motivo por el cual el paciente acudió a consulta
    motivo_consulta = models.TextField(verbose_name="Motivo de Consulta")
    # Descripción detallada de los síntomas que presenta el paciente
    sintomas = models.TextField(verbose_name="Sintomas")
    # Plan de tratamiento o recomendaciones dadas al paciente
    tratamiento = models.TextField(verbose_name="Plan de Tratamiento")
    # Relación con el modelo Diagnóstico, permite asociar uno o varios diagnósticos a la atención médica
    diagnostico = models.ManyToManyField(Diagnostico, verbose_name="Diagnósticos",related_name="diagnosticos_atencion")
    # Detalle del examen físico realizado
    examen_fisico = models.TextField(null=True, blank=True, verbose_name="Examen Físico")
    # Detalle de  examenes a enviar
    examenes_enviados = models.TextField(null=True, blank=True, verbose_name="Examenes enviados")
    # Comentarios adicionales del doctor sobre la atención o el estado del paciente
    comentario_adicional = models.TextField(null=True, blank=True, verbose_name="Comentario")

    @property
    def get_diagnosticos(self):
        return " - ".join([c.descripcion for c in self.diagnostico.all().order_by('descripcion')])
    
    @property
    def calcular_imc(self):
        """Calcula el Índice de Masa Corporal (IMC) basado en el peso y la altura."""
        if self.peso and self.altura and self.altura > 0:
            return round(float(self.peso) / (float(self.altura) ** 2), 2)
        else:
            return None
        

    def __str__(self):
        return f"Atención de {self.paciente} el {self.fecha_atencion}"

    
    class Meta:
        # Ordena las atenciones por fecha de forma descendente
        ordering = ['-fecha_atencion']
        # Nombre singular y plural del modelo en la interfaz administrativa
        verbose_name = "Atención"
        verbose_name_plural = "Atenciones"

# Modelo que representa el detalle de una atención médica.
# Relaciona cada atención con los medicamentos recetados y su cantidad.
class DetalleAtencion(models.Model):
    # Relación con el modelo CabeceraAtencion, indica a qué atención pertenece este detalle
    atencion = models.ForeignKey(Atencion, on_delete=models.CASCADE, verbose_name="Cabecera de Atención",related_name="atenciones")
    # Relación con el modelo Medicamento, indica qué medicamento fue recetado en esta atención
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE, verbose_name="Medicamento",related_name="medicamentos")
   
    # Cantidad de medicamento recetado
    cantidad = models.PositiveIntegerField(verbose_name="Cantidad")
    # Prescripción o indicaciones sobre cómo tomar el medicamento
    prescripcion = models.TextField(verbose_name="Prescripción")
    # Campo adicional: duración del tratamiento con el medicamento (en días)
    duracion_tratamiento = models.PositiveIntegerField(verbose_name="Duración del Tratamiento (días)", null=True, blank=True)

    def __str__(self):
        return f"Detalle de {self.medicamento} para {self.atencion}"

    class Meta:
        # Ordena los detalles por cabecera de atención
        ordering = ['atencion']
        # Nombre singular y plural del modelo en la interfaz administrativa
        verbose_name = "Detalle de Atención"
        verbose_name_plural = "Detalles de Atención"


# Modelo que representa un servicio adicional ofrecido durante una atención médica.
# Puede incluir exámenes, procedimientos, o cualquier otro servicio.
class ServiciosAdicionales(models.Model):
    # Nombre del servicio (ej. Radiografía, Laboratorio, Procedimiento menor, etc.)
    nombre_servicio = models.CharField(max_length=255, verbose_name="Nombre del Servicio")
    # Costo unitario del servicio adicional
    costo_servicio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Costo del Servicio")
    # Descripción opcional sobre el servicio adicional
    descripcion = models.TextField(null=True, blank=True, verbose_name="Descripción del Servicio")

    activo = models.BooleanField(default=True,verbose_name="Activo")
    
    def __str__(self):
        return self.nombre_servicio

    class Meta:
        # Ordena los servicios por nombre
        ordering = ['nombre_servicio']
        # Nombre singular y plural del modelo en la interfaz administrativa
        verbose_name = "Servicio Adicional"
        verbose_name_plural = "Servicios Adicionales"

# Modelo que representa los costos asociados a una atención médica,
# incluyendo consulta, servicios adicionales (exámenes, procedimientos), y otros costos.
class CostosAtencion(models.Model):
    # Relación con el modelo CabeceraAtencion, indica a qué atención médica pertenece el costo
    atencion = models.ForeignKey(Atencion, on_delete=models.PROTECT, verbose_name="Atención",related_name="costos_atencion")
    # Total de los costos calculado
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total", default=0.00)
    # Fecha en que se registraron los costos
    fecha_pago = models.DateTimeField(auto_now_add=True, verbose_name="Fecha Pago")
    
    activo = models.BooleanField(default=True,verbose_name="Activo")
    
    def __str__(self):
        return f"{self.atencion} - Total: {self.total}"

    class Meta:
        # Ordena los costos por fecha de registro
        ordering = ['-fecha_pago']
        # Nombre singular y plural del modelo en la interfaz administrativa
        verbose_name = "Costo de Atención"
        verbose_name_plural = "Costos de Atención"


class CostoAtencionDetalle(models.Model):
    costo_atencion = models.ForeignKey(CostosAtencion, on_delete=models.PROTECT, verbose_name="Costo Atención",related_name="costos_atenciones")
    # Relación ManyToMany con los servicios adicionales utilizados durante la atención
    servicios_adicionales = models.ForeignKey(ServiciosAdicionales, on_delete=models.PROTECT, verbose_name="Servicios Adicionales",related_name="servicios_adicionales")
    # Costo unitario del servicio adicional
    costo_servicio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Costo del Servicio")

    def __str__(self):
        return f"{self.servicios_adicionales} Costo: {self.costo_servicio}"

    class Meta:
         # Nombre singular y plural del modelo en la interfaz administrativa
        verbose_name = "Costo detalle Atención"
        verbose_name_plural = "Costos detalles Atención"


