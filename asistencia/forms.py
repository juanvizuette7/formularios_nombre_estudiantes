from django import forms
from .models import Asistencia

class AsistenciaForm(forms.ModelForm):
    """Formulario basado en el modelo Asistencia."""
    
    class Meta:
        model = Asistencia
        fields = [
            'nombre_completo',
            'documento_identidad', 
            'correo_electronico',
            'fecha_asistencia',
            'hora_ingreso',
            'hora_salida',
            'presente',
            'observaciones'
        ]
        
        widgets = {
            'nombre_completo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Juan Pérez García'
            }),
            'documento_identidad': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 12345678'
            }),
            'correo_electronico': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: juan@correo.com'
            }),
            'fecha_asistencia': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'hora_ingreso': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time'
            }),
            'hora_salida': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time'
            }),
            'presente': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'observaciones': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Comentarios adicionales (opcional)'
            })
        }