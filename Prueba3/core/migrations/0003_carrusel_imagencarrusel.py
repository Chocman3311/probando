# Generated by Django 3.2.4 on 2021-07-08 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_carrusel_imagencarrusel'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrusel',
            name='imagenCarrusel',
            field=models.ImageField(null=True, upload_to='ImgCarrusel'),
        ),
    ]
