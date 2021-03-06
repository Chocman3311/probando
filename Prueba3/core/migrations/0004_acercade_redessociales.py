# Generated by Django 3.2.4 on 2021-07-09 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_carrusel_imagencarrusel'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcercaDe',
            fields=[
                ('idAcercade', models.IntegerField(primary_key=True, serialize=False, verbose_name='id_acercade')),
                ('imagenLogo', models.ImageField(null=True, upload_to='img')),
                ('textoAcercade', models.CharField(max_length=700, verbose_name='Texto_Acercade')),
                ('textoSiguenos', models.CharField(max_length=30, verbose_name='Texto_Siguenos')),
            ],
        ),
        migrations.CreateModel(
            name='RedesSociales',
            fields=[
                ('idRedes', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id_redes')),
                ('imagenRedes', models.ImageField(null=True, upload_to='img')),
            ],
        ),
    ]
