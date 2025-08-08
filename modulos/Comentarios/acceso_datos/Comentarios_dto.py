
class ComentarioDTO:
    def __init__(self, id=None, id_barbero=None, cliente_nombre="", contenido="", calificacion=0, fecha_creacion=None):
        self.id = id
        self.id_barbero = id_barbero
        self.cliente_nombre = cliente_nombre
        self.contenido = contenido
        self.calificacion = calificacion
        self.fecha_creacion = fecha_creacion 

    def __str__(self):
        return (f"ComentarioDTO(id={self.id}, id_barbero={self.id_barbero}, cliente_nombre='{self.cliente_nombre}', "
                f"contenido='{self.contenido}', calificacion={self.calificacion}, fecha_creacion={self.fecha_creacion}")
