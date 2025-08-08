from modulos.Comentarios.acceso_datos.Comentarios_dao import ComentarioDAOPostgres
from modulos.Comentarios.acceso_datos.dao_factory import ComentarioDAOFactory

class PostgresComentarioDAOFactory(ComentarioDAOFactory):
    def crear_dao(self):
        return ComentarioDAOPostgres()
