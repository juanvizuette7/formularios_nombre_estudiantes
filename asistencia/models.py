from django.db import models

class Asistencia(models.Model):
    """Modelo para el registro de asistencia de personas."""
    
    nombre_completo = models.CharField(
        max_length=200,
        verbose_name="Nombre Completo"
    )
    
    documento_identidad = models.CharField(
        max_length=20,
        verbose_name="Documento de Identidad"
    )
    
    correo_electronico = models.EmailField(
        verbose_name="Correo Electrónico"
    )
    
    fecha_asistencia = models.DateField(
        verbose_name="Fecha de Asistencia"
    )
    
    hora_ingreso = models.TimeField(
        verbose_name="Hora de Ingreso"
    )
    
    hora_salida = models.TimeField(
        verbose_name="Hora de Salida",
        blank=True,
        null=True
    )
    
    presente = models.BooleanField(
        default=True,
        verbose_name="Presente"
    )
    
    observaciones = models.TextField(
        blank=True,
        null=True,
        verbose_name="Observaciones"
    )
    
    fecha_registro = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de Registro"
    )
    
    def __str__(self):
        return f"{self.nombre_completo} - {self.fecha_asistencia}"
    
    class Meta:
        verbose_name = "Asistencia"
        verbose_name_plural = "Asistencias"
        ordering = ['-fecha_asistencia', '-hora_ingreso']
