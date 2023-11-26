from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    legajo = models.IntegerField()
    email = models.EmailField()
    alumno = {
        "nombre": "Bautista",
        "apellido": "Kindt",
        "legajo": 123456
    }
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.legajo}"


class Asignatura(models.Model):
    nombre = models.CharField(max_length=40)
    comision = models.IntegerField
    def __str__(self):
        return f"{self.nombre} - {self.comision}"


class Actividades(models.Model):
    nombre = models.CharField(max_length=30)
    limite = models.DateField()
    entregado = models.BooleanField()
    condicion = models.BooleanField()