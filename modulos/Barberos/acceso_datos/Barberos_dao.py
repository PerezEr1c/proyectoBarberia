from modulos.Barberos.acceso_datos.Barberos_dto import BarberoDTO
from modulos.Barberos.acceso_datos.conexion import ConexionDB

class BarberoDAOMySQL:
    
    def guardar(self, barbero_dto):
        conn = ConexionDB().obtener_conexion()
        try:
            with conn.cursor() as cursor:
                sql = "INSERT INTO barberos (nombre, experiencia_anios, especialidad, id_barberia) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (
                    barbero_dto.nombre,
                    barbero_dto.experiencia_anios,
                    barbero_dto.especialidad,
                    barbero_dto.id_barberia
                ))
            conn.commit()
        except Exception as e:
            print(f"[ERROR] guardar(): {e}")
            conn.rollback()
            raise
        finally:
            conn.close()

    def obtener_todos(self):
        conn = ConexionDB().obtener_conexion()
        try:
            with conn.cursor() as cursor:
                cursor.execute("SELECT id, nombre, experiencia_anios, especialidad, id_barberia, fecha_creacion FROM barberos")
                rows = cursor.fetchall()
                return [
                    BarberoDTO(
                        id=row[0], 
                        nombre=row[1], 
                        experiencia_anios=row[2], 
                        especialidad=row[3], 
                        id_barberia=row[4], 
                        fecha_creacion=row[5]
                    )
                    for row in rows
                ]
        except Exception as e:
            print(f"[ERROR] obtener_todos(): {e}")
            raise
        finally:
            conn.close()

    def obtener_por_id(self, id):
        conn = ConexionDB().obtener_conexion()
        try:
            with conn.cursor() as cursor:
                cursor.execute("SELECT id, nombre, experiencia_anios, especialidad, id_barberia, fecha_creacion FROM barberos WHERE id = %s", (id,))
                row = cursor.fetchone()
                if row:
                    return BarberoDTO(
                        id=row[0], 
                        nombre=row[1], 
                        experiencia_anios=row[2], 
                        especialidad=row[3], 
                        id_barberia=row[4], 
                        fecha_creacion=row[5]
                    )
                return None
        except Exception as e:
            print(f"[ERROR] obtener_por_id(): {e}")
            raise
        finally:
            conn.close()

    def actualizar(self, barbero_dto):
        conn = ConexionDB().obtener_conexion()
        try:
            with conn.cursor() as cursor:
                sql = "UPDATE barberos SET nombre = %s, experiencia_anios = %s, especialidad = %s, id_barberia = %s WHERE id = %s"
                cursor.execute(sql, (
                    barbero_dto.nombre,
                    barbero_dto.experiencia_anios,
                    barbero_dto.especialidad,
                    barbero_dto.id_barberia,
                    barbero_dto.id
                ))
            conn.commit()
        except Exception as e:
            print(f"[ERROR] actualizar(): {e}")
            conn.rollback()
            raise
        finally:
            conn.close()

    def eliminar(self, id):
        conn = ConexionDB().obtener_conexion()
        try:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM barberos WHERE id = %s", (id,))
            conn.commit()
        except Exception as e:
            print(f"[ERROR] eliminar(): {e}")
            conn.rollback()
            raise
        finally:
            conn.close()

class BarberoDAOPostgres(BarberoDAOMySQL):
    pass
