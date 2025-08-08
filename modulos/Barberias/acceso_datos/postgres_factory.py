from modulos.Barberias.acceso_datos.Barberias_dao import BarberiaDAOPostgres
from modulos.Barberias.acceso_datos.dao_factory import BarberiaDAOFactory

class PostgresBarberiaDAOFactory(BarberiaDAOFactory):
    def crear_dao(self):
        return BarberiaDAOPostgres()
