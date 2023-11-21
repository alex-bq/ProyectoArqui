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

    class Meta:
        db_table = "dueno"


class Vehiculo(models.Model):
    patente = models.CharField(max_length=6, primary_key=True)
    marca = models.CharField(max_length=35)
    modelo = models.CharField(max_length=35)
    color = models.CharField(max_length=35)
    run_cli = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    class Meta:
        db_table = "vehiculo"


class Tarjeta(models.Model):
    num_tarjeta = models.CharField(max_length=16, primary_key=True)
    cvv = models.CharField(max_length=3)
    run_cli = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    class Meta:
        db_table = "tarjeta"


class Direccion(models.Model):
    id_dir = models.IntegerField(primary_key=True)
    nombre_dic = models.CharField(max_length=50)

    class Meta:
        db_table = "direccion"


class Estacionamiento(models.Model):
    id_est = models.IntegerField(primary_key=True)
    tarifa = models.IntegerField()
    run_due = models.ForeignKey(Dueno, on_delete=models.CASCADE)
    id_dir = models.OneToOneField(Direccion, on_delete=models.CASCADE)

    class Meta:
        db_table = "estacionamiento"


class Arriendo(models.Model):
    id_arr = models.IntegerField(primary_key=True)
    hora_inic = models.DateTimeField()
    hora_fin = models.DateTimeField()
    patente = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    id_est = models.ForeignKey(Estacionamiento, on_delete=models.CASCADE)

    class Meta:
        db_table = "arriendo"
