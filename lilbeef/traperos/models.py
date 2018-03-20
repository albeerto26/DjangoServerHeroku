from django.db import models

# Create your models here.


class Trapero(models.Model):
    aka = models.CharField(max_length=100)
    nombre = models.CharField(max_length=250, blank=True, null=True)
    apellidos = models.CharField(max_length=250, blank=True, null=True)
    edad = models.IntegerField(default=0)
    foto = models.FileField(upload_to='fotos/', default='logos/anonymous.jpg')


class Disco(models.Model):
    nombre = models.CharField(max_length=250)
    fecha_publicacion = models.DateField()
    trapero = models.ForeignKey('Trapero', on_delete=models.CASCADE, related_name='disco_trapero')
    portada = models.FileField(upload_to='portadas/', default='logos/disco_vacio.jpg')


class Tiraera(models.Model):
    trapero_tira = models.ForeignKey('Trapero', on_delete=models.CASCADE, related_name='trapero_tirador')
    trapero_recibe = models.ForeignKey('Trapero', on_delete=models.CASCADE, related_name='trapero_recibor')
    fecha_inicio = models.DateField()
    descripcion = models.TextField()