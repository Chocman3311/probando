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
    imagenLogo = models.ImageField(upload_to = "img", null=True)
    textoAcercade = models.CharField(max_length=700, verbose_name="Texto_Acercade" )   
    textoSiguenos = models.CharField(max_length=30, verbose_name="Texto_Siguenos")
    fotoSiguenos = models.ImageField(upload_to = "img", null=True)
    def __str__(self):
        return self.textoAcercade
