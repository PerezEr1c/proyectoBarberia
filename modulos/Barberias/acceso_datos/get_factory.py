from modulos.Barberias.configuracion.config import cargar_configuracion
from modulos.Barberias.acceso_datos.mysql_factory import MySQLBarberiaDAOFactory
from modulos.Barberias.acceso_datos.postgres_factory import PostgresBarberiaDAOFactory

def obtener_fabrica_barberia():
    config = cargar_configuracion()
    if config["db_engine"] == "postgres":
        return PostgresBarberiaDAOFactory()
    return MySQLBarberiaDAOFactory()
