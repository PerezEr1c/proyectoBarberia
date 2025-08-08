from modulos.Barberos.acceso_datos.Barberos_dao import BarberoDAOPostgres
from modulos.Barberos.acceso_datos.dao_factory import BarberoDAOFactory

class PostgresBarberoDAOFactory(BarberoDAOFactory):
    def crear_dao(self):
        return BarberoDAOPostgres()
