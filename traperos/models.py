"""Modelos de Django."""
from django.db import models
"""Manejos de fechas."""
import datetime
# Create your models here.

class Trapero(models.Model):
    """Modelo con informacion sobre los traperos."""

    aka = models.CharField(max_length=100)
    nombre_real = models.CharField(max_length=250, blank=True, null=True)
    ano_nacimiento = models.IntegerField(default=1980)
    foto = models.FileField(upload_to='fotos/', default='logos/anonymous.jpg')

    @property
    def edad(self):
        """Devuelve la edad aproximada usando el ano actual como base."""
        ano_actual = datetime.datetime.now().year
        return '{0}'.format(ano_actual - self.ano_nacimiento)

    def __str__(self):
        """Conversion de objeto a cadena humana."""
        return '{0}'.format(self.aka)


class Disco(models.Model):
    """Modelo con informacion sobre los discos."""

    nombre = models.CharField(max_length=250)
    fecha_publicacion = models.DateField()
    portada = models.FileField(upload_to='portadas/', default='img/disco.jpg')
    trapero = models.ForeignKey('Trapero', on_delete=models.CASCADE, related_name='disco_trapero')

    def __str__(self):
        """Conversion de objeto a cadena humana."""
        return '{0} - {1}'.format(self.nombre, self.trapero.aka)


class Tiraera(models.Model):
    """Modelo con informacion sobre las tiraeras entre traperos."""

    titulo = models.CharField(max_length=250)
    fecha_inicio = models.DateField()
    descripcion = models.TextField()
    trapero_tira = models.ForeignKey('Trapero', on_delete=models.CASCADE, related_name='trapero_tirador')
    trapero_recibe = models.ForeignKey('Trapero', on_delete=models.CASCADE, related_name='trapero_recibor')

    def __str__(self):
        """Conversion de objeto a cadena humana."""
        return '{0}'.format(self.titulo)


class Alerta(models.Model):
    """Modelo para recibir alertas de usuarios a traves del formulario."""

    titulo = models.CharField(max_length=250)
    fecha_alerta = models.DateField(auto_now_add=True)
    descripcion = models.TextField()
    trapero = models.ForeignKey('Trapero', on_delete=models.CASCADE, related_name='alertas_traperos')

    def __str__(self):
        """Conversion de objeto a cadena humana."""
        return '{0}'.format(self.titulo)
