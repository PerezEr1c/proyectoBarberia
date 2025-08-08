from modulos.Barberos.acceso_datos.Barberos_dao import BarberoDAOMySQL
from modulos.Barberos.acceso_datos.dao_factory import BarberoDAOFactory

class MySQLBarberoDAOFactory(BarberoDAOFactory):
    def crear_dao(self):
        return BarberoDAOMySQL()
