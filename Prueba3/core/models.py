from django.db import models

# Create your models here.
class Carrusel(models.Model):
    idCarrusel = models.IntegerField(primary_key=True, verbose_name= "id_carrusel")
    textoCarrusel = models.CharField(max_length=50, verbose_name="Texto_carrusel")
    imagenCarrusel = models.ImageField(upload_to = "ImgCarrusel", null=True)

    def __str__(self):
        return self.textoCarrusel