# Importamos el DTO que representa las barberías y la clase de conexión a la base de datos
from modulos.Barberias.acceso_datos.Barberias_dto import BarberiaDTO
from modulos.Barberias.acceso_datos.conexion import ConexionDB

# Obtenemos una instancia de conexión a la base de datos (compartida por ambos DAOs)
conn = ConexionDB().obtener_conexion()

# DAO para base de datos MySQL
class BarberiaDAOMySQL:
    def guardar(self, barberia_dto):
        with conn.cursor() as cursor:
            sql = "INSERT INTO barberias (nombre, direccion, telefono, email) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (
                barberia_dto.nombre,
                barberia_dto.direccion,
                barberia_dto.telefono,
                barberia_dto.email
            ))
        conn.commit()

    def obtener_todos(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, nombre, direccion, telefono, email, fecha_creacion FROM barberias")
            rows = cursor.fetchall()
        return [
            BarberiaDTO(id=row[0], nombre=row[1], direccion=row[2], telefono=row[3], email=row[4], fecha_creacion=row[5])
            for row in rows
        ]

    def obtener_por_id(self, id):
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, nombre, direccion, telefono, email, fecha_creacion FROM barberias WHERE id = %s", (id,))
            row = cursor.fetchone()
        if row:
            return BarberiaDTO(id=row[0], nombre=row[1], direccion=row[2], telefono=row[3], email=row[4], fecha_creacion=row[5])
        return None

    def actualizar(self, barberia_dto):
        with conn.cursor() as cursor:
            sql = "UPDATE barberias SET nombre = %s, direccion = %s, telefono = %s, email = %s WHERE id = %s"
            cursor.execute(sql, (
                barberia_dto.nombre,
                barberia_dto.direccion,
                barberia_dto.telefono,
                barberia_dto.email,
                barberia_dto.id
            ))
        conn.commit()

    def eliminar(self, id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM barberias WHERE id = %s", (id,))
        conn.commit()

# DAO para base de datos PostgreSQL (misma lógica, diferente backend)
class BarberiaDAOPostgres:
    def guardar(self, barberia_dto):
        with conn.cursor() as cursor:
            sql = "INSERT INTO barberias (nombre, direccion, telefono, email) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (
                barberia_dto.nombre,
                barberia_dto.direccion,
                barberia_dto.telefono,
                barberia_dto.email
            ))
        conn.commit()

    def obtener_todos(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, nombre, direccion, telefono, email, fecha_creacion FROM barberias")
            rows = cursor.fetchall()
        return [
            BarberiaDTO(id=row[0], nombre=row[1], direccion=row[2], telefono=row[3], email=row[4], fecha_creacion=row[5])
            for row in rows
        ]

    def obtener_por_id(self, id):
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, nombre, direccion, telefono, email, fecha_creacion FROM barberias WHERE id = %s", (id,))
            row = cursor.fetchone()
        if row:
            return BarberiaDTO(id=row[0], nombre=row[1], direccion=row[2], telefono=row[3], email=row[4], fecha_creacion=row[5])
        return None

    def actualizar(self, barberia_dto):
        with conn.cursor() as cursor:
            sql = "UPDATE barberias SET nombre = %s, direccion = %s, telefono = %s, email = %s WHERE id = %s"
            cursor.execute(sql, (
                barberia_dto.nombre,
                barberia_dto.direccion,
                barberia_dto.telefono,
                barberia_dto.email,
                barberia_dto.id
            ))
        conn.commit()

    def eliminar(self, id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM barberias WHERE id = %s", (id,))
        conn.commit()
