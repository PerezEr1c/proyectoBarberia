class BarberiaDTO:
    # Constructor de la clase, inicializa los atributos de la barbería
    def __init__(self, id=None, nombre="", direccion="", telefono="", email="", fecha_creacion=None):
        self.id = id                                # ID de la barbería (None si es nueva)
        self.nombre = nombre                        # Nombre de la barbería
        self.direccion = direccion                  # Dirección física
        self.telefono = telefono                    # Teléfono de contacto
        self.email = email                          # Correo electrónico
        self.fecha_creacion = fecha_creacion        # Fecha de creación (puede ser None, lo asigna la DB)

    # Representación en texto del objeto, útil para imprimir o depurar
    def __str__(self):
        return (f"BarberiaDTO(id={self.id}, nombre='{self.nombre}', direccion='{self.direccion}', "
                f"telefono='{self.telefono}', email='{self.email}', fecha_creacion={self.fecha_creacion})")
