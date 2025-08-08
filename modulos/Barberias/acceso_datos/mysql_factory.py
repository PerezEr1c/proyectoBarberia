from modulos.Barberias.acceso_datos.Barberias_dao import BarberiaDAOMySQL
from modulos.Barberias.acceso_datos.dao_factory import BarberiaDAOFactory

class MySQLBarberiaDAOFactory(BarberiaDAOFactory):
    def crear_dao(self):
        return BarberiaDAOMySQL()
