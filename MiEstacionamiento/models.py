from django.db import models
from django.contrib.auth.models import User

class Marca(models.Model):
    nombre_marca = models.CharField(max_length=35)

    def __str__(self):
        return self.nombre_marca

    class Meta:
        db_table = "marca"


class Modelo(models.Model):
    nombre_modelo = models.CharField(max_length=35)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.marca} - {self.nombre_modelo}"

    class Meta:
        db_table = "modelo"


class Vehiculo(models.Model):
    patente = models.CharField(max_length=6, primary_key=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    color = models.CharField(max_length=35)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.patente} - {self.marca} {self.modelo}"

    class Meta:
        db_table = "vehiculo"



class Tarjeta(models.Model):
    num_tarjeta = models.CharField(max_length=16, primary_key=True)
    cvv = models.CharField(max_length=3)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.num_tarjeta} - {self.user}"

    class Meta:
        db_table = "tarjeta"


class Estacionamiento(models.Model):
    ESTADOS = [
        ("ocupado", "Ocupado"),
        ("disponible", "Disponible"),
        ("cerrado", "Cerrado"),
    ]
    id = models.AutoField(primary_key=True)
    valorMinu = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=255)
    estado = models.CharField(max_length=20, choices=ESTADOS, default="disponible")

    def save(self, *args, **kwargs):
        if not self.id:
            # Genera automáticamente el valor del campo id
            self.id = Estacionamiento.objects.count() + 1
        super().save(*args, **kwargs)


class Arriendo(models.Model):


    id = models.IntegerField(primary_key=True)
    hora_inic = models.DateTimeField()
    hora_fin = models.DateTimeField()
    patente = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    estacionamiento = models.ForeignKey(Estacionamiento, on_delete=models.CASCADE)
    


    def __str__(self):
        return f"{self.id} - {self.patente} - {self.estacionamiento} "

    class Meta:
        db_table = "arriendo"


class Calificacion(models.Model):
    cali = models.AutoField(primary_key=True)
    arriendo = models.OneToOneField(Arriendo, on_delete=models.CASCADE)
    puntaje = models.IntegerField()
    comentario = models.TextField()

    def __str__(self):
        return f"Calificación para Arriendo {self.arriendo}"

    class Meta:
        db_table = "calificacion"

class arriendoWardado(models.Model):
    ESTATUS = [
        ("pendiente", "Pendiente"),
        ("cancelado", "Cancelado"),
        ("culminado", "Culminado"),
    ]
    id = models.AutoField(primary_key=True)
    hora_inic = models.DateTimeField()
    hora_fin = models.DateTimeField()
    patente = models.CharField(max_length=6)
    estatus = models.estado = models.CharField(max_length=20, choices=ESTATUS, default="pendiente")

    def __str__(self):
        return f"{self.id} - {self.patente} - {self.estatus}"

    class Meta:
        db_table = "arriendoWardado"


