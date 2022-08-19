"""Jardin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from inicio import views
from registros import views as views_registros
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.principal, name='Principal'),
    path('contacto/', views_registros.contacto, name='Contacto'),
    path('pendientes/', views_registros.pendientes, name='Pendientes'),
    path('ninos/', views_registros.ninos, name='Ninos'),
    path('entregables/', views_registros.entregables, name='Entregables'),
    path('archivos/', views_registros.archivos, name='SubirEntregables'),
    path('registrarDuda/', views_registros.registrarDuda, name='RegistrarDuda'),
    path('editarDuda/<int:id>', views_registros.editarDuda, name='EditarDuda'),
    path('consultarDuda/<int:id>', views_registros.consultarDuda, name='ConsultarDuda'),
    path('eliminarDuda/<int:id>', views_registros.eliminarDuda, name='EliminarDuda'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    