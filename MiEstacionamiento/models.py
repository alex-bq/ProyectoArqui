from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=35)
    aPaterno = models.CharField(max_length=35)
    run = models.IntegerField(primary_key=True)
    dv = models.CharField(max_length=1)
    correo = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.ap_paterno}"

    class Meta:
        db_table = "cliente"


class Dueno(models.Model):
    nombre = models.CharField(max_length=35)
    aPaterno = models.CharField(max_length=35)
    run = models.IntegerField(primary_key=True)
    dv = models.CharField(max_length=1)
    correo = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.ap_paterno}"

    class Meta:
        db_table = "dueno"


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
    run = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.patente} - {self.marca} {self.modelo}"

    class Meta:
        db_table = "vehiculo"


class Tarjeta(models.Model):
    num_tarjeta = models.CharField(max_length=16, primary_key=True)
    cvv = models.CharField(max_length=3)
    run = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.num_tarjeta} - {self.run}"

    class Meta:
        db_table = "tarjeta"


class Direccion(models.Model):
    id = models.IntegerField(primary_key=True)
    direc = models.CharField(max_length=50)

    def __str__(self):
        return self.direc

    class Meta:
        db_table = "direccion"


class Estacionamiento(models.Model):
    id = models.IntegerField(primary_key=True)
    tarifa = models.IntegerField()
    run = models.ForeignKey(Dueno, on_delete=models.CASCADE)
    id_dir = models.OneToOneField(Direccion, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} - {self.run} - {self.id_dir}"

    class Meta:
        db_table = "estacionamiento"


class Arriendo(models.Model):
    ESTADOS = [
        ("pendiente", "Pendiente"),
        ("cancelado", "Cancelado"),
        ("culminado", "Culminado"),
    ]

    id = models.IntegerField(primary_key=True)
    hora_inic = models.DateTimeField()
    hora_fin = models.DateTimeField()
    patente = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    id_est = models.ForeignKey(Estacionamiento, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=ESTADOS, default="pendiente")

    def __str__(self):
        return f"{self.id} - {self.patente} - {self.id_est} - {self.estado}"

    class Meta:
        db_table = "arriendo"


class Calificacion(models.Model):
    cali = models.AutoField(primary_key=True)
    id = models.OneToOneField(Arriendo, on_delete=models.CASCADE)
    puntaje = models.IntegerField()
    comentario = models.TextField()

    def __str__(self):
        return f"Calificación para Arriendo {self.id}"

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


