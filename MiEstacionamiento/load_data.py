from datetime import datetime
from django.core.management import call_command
from MiEstacionamiento.models import (
    Cliente,
    Dueno,
    Vehiculo,
    Tarjeta,
    Direccion,
    Estacionamiento,
    Arriendo,
)


def load_data():
    # Crea instancias de tus modelos con los datos deseados
    cliente = Cliente.objects.create(
        run_cli=24352753,
        dv_run="2",
        nombre="Andie",
        s_nombre="Wally",
        ap_paterno="Daugherty",
        ap_materno="Pestor",
        fec_nac=datetime.strptime("1995-10-14", "%Y-%m-%d"),
        correo="wpestor0@chicagotribune.com",
        clave="tB5Qp@z3ZhuKs18",
    )

    dueno = Dueno.objects.create(
        run_due=12345678,
        dv_run="3",
        nombre="Ejemplo",
        s_nombre="Segundo Nombre",
        ap_paterno="ApellidoPaterno",
        ap_materno="ApellidoMaterno",
        fec_nac=datetime.strptime("1990-01-01", "%Y-%m-%d"),
        correo="dueno@example.com",
        clave="clave_secreta",
    )

    vehiculo = Vehiculo.objects.create(
        patente="ABC123",
        marca="Toyota",
        modelo="Corolla",
        color="Rojo",
        run_cli=cliente,
    )

    tarjeta = Tarjeta.objects.create(
        num_tarjeta="1111222233334444", cvv="123", run_cli=cliente
    )

    direccion = Direccion.objects.create(id_dir=1, nombre_dic="Calle Principal")

    estacionamiento = Estacionamiento.objects.create(
        id_est=1, tarifa=10, run_due=dueno, id_dir=direccion
    )

    arriendo = Arriendo.objects.create(
        id_arr=1,
        hora_inic=datetime.strptime("2023-11-09T12:00:00", "%Y-%m-%dT%H:%M:%S"),
        hora_fin=datetime.strptime("2023-11-09T14:00:00", "%Y-%m-%dT%H:%M:%S"),
        patente=vehiculo,
        id_est=estacionamiento,
    )

    print("Datos cargados exitosamente.")


if __name__ == "__main__":
    # Llama a la función load_data para cargar los datos
    load_data()
