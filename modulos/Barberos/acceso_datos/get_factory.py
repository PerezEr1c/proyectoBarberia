from modulos.Barberos.configuracion.config import cargar_configuracion
from modulos.Barberos.acceso_datos.mysql_factory import MySQLBarberoDAOFactory
from modulos.Barberos.acceso_datos.postgres_factory import PostgresBarberoDAOFactory

def obtener_fabrica():
    config = cargar_configuracion()
    if config["db_engine"] == "postgres":
        return PostgresBarberoDAOFactory()
    return MySQLBarberoDAOFactory()
