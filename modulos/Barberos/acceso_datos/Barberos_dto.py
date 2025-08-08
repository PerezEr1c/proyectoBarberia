class BarberoDTO:
    def __init__(self, id=None, nombre="", experiencia_anios=0, especialidad="", id_barberia=None, fecha_creacion=None):
        self.id = id
        self.nombre = nombre
        self.experiencia_anios = experiencia_anios
        self.especialidad = especialidad
        self.id_barberia = id_barberia
        self.fecha_creacion = fecha_creacion

    def __str__(self):
        return (f"BarberoDTO(id={self.id}, nombre='{self.nombre}', experiencia_anios={self.experiencia_anios}, "
                f"especialidad='{self.especialidad}', id_barberia={self.id_barberia}, fecha_creacion={self.fecha_creacion})")
