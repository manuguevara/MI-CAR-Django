from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator

# Create your models here

class Slider(models.Model):
    imagen = models.ImageField(upload_to="Sliders", null=True)

    def __str__(self):
        return self.imagen.name

class Galeria(models.Model):
    imagen = models.ImageField(upload_to="Galeria", null=True)

    def __str__(self):
        return self.imagen.name

class MisionVision(models.Model):
    texto1 = models.CharField(max_length=250)
    texto2 = models.CharField(max_length=250, null=True)
    imagen = models.ImageField(upload_to="Mision y Visión",null=True)
    mision = models.CharField(max_length=300)
    vision = models.CharField(max_length=300)

    def __str__(self):
        return "Misión y Visión"

class Insumo(models.Model):
    nombre = models.CharField(validators=[MinLengthValidator(3)],max_length=120, unique=True)
    precio = models.IntegerField(validators=[MinValueValidator(1)])
    imagen = models.ImageField(upload_to="Insumo", null=True)
    descripcion = models.TextField(validators=[MinLengthValidator(3)],max_length=200,null=True)
    stock = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.nombre 

