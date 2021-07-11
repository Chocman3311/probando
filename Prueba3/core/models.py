from django.db import models

# Create your models here.

# Creacion de tablas que contienen datos como imagenes o textos
class Carrusel(models.Model):
    idCarrusel = models.IntegerField(primary_key=True, verbose_name= "id_carrusel")
    textoCarrusel = models.CharField(max_length=50, verbose_name="Texto_carrusel")
    imagenCarrusel = models.ImageField(upload_to = "ImgCarrusel", null=True)

    def __str__(self):
        return self.textoCarrusel


class AcercaDe(models.Model):
    idAcercade = models.IntegerField(primary_key=True, verbose_name="id_acercade")
    imagenLogo = models.ImageField(upload_to = "imgLogo", null=True)
    textoAcercade = models.CharField(max_length=700, verbose_name="Texto_Acercade" )   
    textoSiguenos = models.CharField(max_length=30, verbose_name="Texto_Siguenos")
    fotoSiguenos = models.ImageField(upload_to = "imgRedes", null=True)
    def __str__(self):
        return self.textoAcercade


class FormularioContacto(models.Model):
    idFormulario = models.IntegerField(primary_key=True, verbose_name="IdFormulario")
    nombreFormulario = models.CharField(max_length=20, verbose_name="Nombre")
    apellidoFormulario = models.CharField(max_length=20, verbose_name="Apellido")
    emailFormulario = models.CharField(max_length=20, verbose_name="Email")
    comentarioFormulario = models.CharField(max_length=20, verbose_name="Comentario")
    def __str__(self):
        return self.nombreFormulario


class Trabajos(models.Model):
    idCarta = models.IntegerField(primary_key=True, verbose_name="IdCarta")
    imagenTrabajo = models.ImageField(upload_to = "imgTrabajos", null=True)
    tituloTrabajo = models.CharField(max_length=50, verbose_name="Nombre Trabajo")
    diagnostico = models.CharField(max_length=50, verbose_name="Diagnostico")
    mecanico = models.CharField(max_length=50, verbose_name="Mecanico")
    fecha = models.CharField(max_length=30, verbose_name="Fecha")
    listadoMateriales = models.CharField(max_length=100, verbose_name="Listado Materiales")
    def __str__(self):
        return self.mecanico