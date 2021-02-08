from django.db import models

# Create your models here.


class Foto(models.Model):
    class Meta:
        verbose_name_plural = "Fotos"

    nombre = models.CharField(max_length=50)
    ruta_imagen = models.FileField(blank=True)

    def __str__(self):
        return self.nombre
