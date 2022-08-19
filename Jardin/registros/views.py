from django.shortcuts import get_object_or_404, render
from .forms import ContacoFormDuda, ContactoForm, FormArchivos
from .models import Contacto, Entregables, Tareas, ZonaNiños
from django.contrib import messages 


def pendientes(request):
    tareas = Tareas.objects.all()
    return render(request, 'registros/pendientes.html', {'tareas': tareas})

def entregables(request):
    return render(request, 'registros/entregables.html')

def contacto(request):
    dudas = Contacto.objects.all()
    return render(request, 'registros/contacto.html', {'dudas': dudas})

def ninos(request):
    videos = ZonaNiños.objects.all()
    return render(request, 'registros/ninos.html', {'videos': videos})



def registrarDuda(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid(): #Si los datos recibidos son correctos
            form.save() #inserta
            dudas = Contacto.objects.all()
            return render(request,'registros/contacto.html', {'dudas': dudas})
    form = ContactoForm()
    #Si algo sale mal se reenvian al formulario los datos ingresados
    return render(request,'registros/dudas.html',{'form': form})


    # Eliminar Comentario
def eliminarDuda(request, id, 
    confirmacion = 'registros/confirmarEliminacion.html'):
    duda = get_object_or_404(Contacto, id=id)
    if request.method == 'POST':
        duda.delete()
        dudas = Contacto.objects.all()
        return render(request, 'registros/contacto.html', {'dudas': dudas})
    return render(request, confirmacion, {'object': duda})

# Editar

def consultarDuda(request, id):
    duda = Contacto.objects.get(id=id)
    return render(request, 'registros/formEditarDuda.html', {'duda': duda})

def editarDuda(request, id):
    duda = get_object_or_404(Contacto, id=id)
    form = ContacoFormDuda(request.POST, instance=duda)
    if form.is_valid():
            form.save()
            dudas = Contacto.objects.all()
            return render(request, 'registros/contacto.html', {'dudas': dudas})
    return render(request, 'registros/formEditarDuda.html', {'form':form})



def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            nombreAlumno =request.POST['nombreAlumno']
            grupo =request.POST['grupo']
            correo =request.POST['correo']
            nota =request.POST['nota']
            archivo =request.FILES['archivo']
            insert = Entregables(nombreAlumno=nombreAlumno, grupo=grupo, correo=correo, nota=nota, archivo=archivo)
            insert.save()
            return render(request, 'registros/entregables.html')
        else:
            messages.error(request, 'Error al subir el archivo')
    else:
        return render(request, 'registros/entregables.html', {'entregable':Entregables})
    
def consultasSQL(request):
    entregables=Entregables.objects.raw('SELECT id, matricula, nombre, carrera, turno, imagen FROM registros_alumnos where carrera="TI" ORDER BY turno DESC')
    return render (request, 'registros/consultas.html', {'entregables':entregables})