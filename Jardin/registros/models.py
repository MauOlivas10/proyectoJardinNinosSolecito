from django.db import models


class Tareas(models.Model): #Define la estructura de la tabla
    
    nomTarea = models.CharField(max_length=50, verbose_name="Nombre de la tarea")
    clave = models.CharField(max_length=50, verbose_name="Clave")
    descripcion = models.TextField(verbose_name="Descripcion")
    grado = models.CharField(max_length=50, verbose_name="Grado")
    FechaEntrega = models.CharField(max_length=50 ,verbose_name="Fecha de entrega")
    imagen = models.ImageField(null=True, upload_to="fotos", verbose_name="Imagen del Curso")
    created = models.DateTimeField(auto_now_add=True) #Fecha de creacion
    update = models.DateTimeField(auto_now_add=True) #Fecha de actualizacion
    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"
        ordering = ["created"]
    def __str__(self):
        return self.nomTarea

class Entregables(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Clave")
    nombreAlumno = models.CharField(max_length=50, verbose_name="Nombre del Alumno")
    grupo = models.CharField(max_length=50, verbose_name="Grupo")
    correo = models.CharField(max_length=50, verbose_name="Correo")
    nota = models.TextField(verbose_name="Nota")
    archivo = models.FileField(upload_to="archivos", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Subido") #Fecha de creacion
    update = models.DateTimeField(auto_now_add=True, verbose_name="Actualizado") #Fecha de actualizacion
    class Meta:
        verbose_name = "Entregable"
        verbose_name_plural = "Entregables"
        ordering = ["created"]
    def __str__(self):
        return self.nombreAlumno



class Contacto(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Clave")
    nombreP = models.CharField(max_length=50, verbose_name="Nombre del Padre")
    nombreA = models.CharField(max_length=50, verbose_name="Nombre del Alumno")
    telefono = models.CharField(max_length=50, verbose_name="Telefono")
    grupo = models.CharField(max_length=50, verbose_name="Grupo")
    correo = models.CharField(max_length=50, verbose_name="Correo")
    duda = models.TextField(verbose_name="Duda")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Subido") #Fecha de creacion
    update = models.DateTimeField(auto_now_add=True, verbose_name="Actualizado") #Fecha de actualizacion
    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
        ordering = ["created"]
    def __str__(self):
        return self.nombreA

class ZonaNiños(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Clave")
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    enlace = models.TextField(verbose_name="link")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Subido") #Fecha de creacion
    update = models.DateTimeField(auto_now_add=True, verbose_name="Actualizado") #Fecha de actualizacion
    class Meta:
        verbose_name = "Zona de Niños"
        verbose_name_plural = "Zona de Niños"
        ordering = ["created"]
    def __str__(self):
        return self.nombre