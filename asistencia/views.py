from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AsistenciaForm

def registro_asistencia(request):
    """Vista para el registro de asistencia."""
    
    if request.method == 'POST':
        form = AsistenciaForm(request.POST)
        
        if form.is_valid():
            asistencia = form.save()
            messages.success(
                request, 
                f'¡Asistencia registrada correctamente para {asistencia.nombre_completo}!'
            )
            return redirect('asistencia:confirmacion')
        else:
            messages.error(
                request, 
                'Por favor, revise los datos ingresados e intente nuevamente.'
            )
    else:
        form = AsistenciaForm()
    
    return render(request, 'asistencia/registro.html', {'form': form})

def confirmacion_asistencia(request):
    """Vista de confirmación después del registro."""
    return render(request, 'asistencia/confirmacion.html')
