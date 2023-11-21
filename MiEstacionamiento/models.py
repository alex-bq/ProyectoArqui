from django.db import models


class Cliente(models.Model):
    run_cli = models.IntegerField(primary_key=True)
    dv_run = models.CharField(max_length=1)
    nombre = models.CharField(max_length=35)
    s_nombre = models.CharField(max_length=35, null=True, blank=True)
    ap_paterno = models.CharField(max_length=35)
    ap_materno = models.CharField(max_length=35)
    fec_nac = models.DateField()
    correo = models.EmailField()
    clave = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.ap_paterno} {self.ap_materno}"

    class Meta:
        db_table = "cliente"


class Dueno(models.Model):
    run_due = models.IntegerField(primary_key=True)
    dv_run = models.CharField(max_length=1)
    nombre = models.CharField(max_length=35)
    s_nombre = models.CharField(max_length=35, null=True, blank=True)
    ap_paterno = models.CharField(max_length=35)
    ap_materno = models.CharField(max_length=35)
    fec_nac = models.DateField()
    correo = models.EmailField()
    clave = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.ap_paterno} {self.ap_materno}"

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
    run_cli = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.patente} - {self.marca} {self.modelo}"

    class Meta:
        db_table = "vehiculo"


class Tarjeta(models.Model):
    num_tarjeta = models.CharField(max_length=16, primary_key=True)
    cvv = models.CharField(max_length=3)
    run_cli = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.num_tarjeta} - {self.run_cli}"

    class Meta:
        db_table = "tarjeta"


class Direccion(models.Model):
    id_dir = models.IntegerField(primary_key=True)
    nombre_dic = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_dic

    class Meta:
        db_table = "direccion"


class Estacionamiento(models.Model):
    id_est = models.IntegerField(primary_key=True)
    tarifa = models.IntegerField()
    run_due = models.ForeignKey(Dueno, on_delete=models.CASCADE)
    id_dir = models.OneToOneField(Direccion, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id_est} - {self.run_due} - {self.id_dir}"

    class Meta:
        db_table = "estacionamiento"


class Arriendo(models.Model):
    ESTADOS = [
        ("pendiente", "Pendiente"),
        ("cancelado", "Cancelado"),
        ("culminado", "Culminado"),
    ]

    id_arr = models.IntegerField(primary_key=True)
    hora_inic = models.DateTimeField()
    hora_fin = models.DateTimeField()
    patente = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    id_est = models.ForeignKey(Estacionamiento, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=ESTADOS, default="pendiente")

    def __str__(self):
        return f"{self.id_arr} - {self.patente} - {self.id_est} - {self.estado}"

    class Meta:
        db_table = "arriendo"


class Calificacion(models.Model):
    id_calificacion = models.AutoField(primary_key=True)
    id_arr = models.OneToOneField(Arriendo, on_delete=models.CASCADE)
    puntaje = models.IntegerField()
    comentario = models.TextField()

    def __str__(self):
        return f"Calificación para Arriendo {self.id_arr}"

    class Meta:
        db_table = "calificacion"
