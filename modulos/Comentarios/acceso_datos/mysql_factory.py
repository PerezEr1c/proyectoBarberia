from modulos.Comentarios.acceso_datos.Comentarios_dao import ComentarioDAOMySQL
from modulos.Comentarios.acceso_datos.dao_factory import ComentarioDAOFactory

class MySQLComentarioDAOFactory(ComentarioDAOFactory):
    def crear_dao(self):
        return ComentarioDAOMySQL()
