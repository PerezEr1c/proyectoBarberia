from modulos.Comentarios.acceso_datos.Comentarios_dto import ComentarioDTO
from modulos.Comentarios.acceso_datos.conexion import ConexionDB

class ComentarioDAOMySQL:

    def guardar(self, comentario_dto):
        conn = ConexionDB().obtener_conexion()
        try:
            with conn.cursor() as cursor:
                sql = """INSERT INTO comentarios (id_barbero, cliente_nombre, contenido, calificacion)
                         VALUES (%s, %s, %s, %s)"""
                cursor.execute(sql, (
                    comentario_dto.id_barbero,
                    comentario_dto.cliente_nombre,
                    comentario_dto.contenido,
                    comentario_dto.calificacion
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
                cursor.execute("""SELECT id, id_barbero, cliente_nombre, contenido, calificacion, fecha_creacion 
                                  FROM comentarios""")
                rows = cursor.fetchall()
                return [
                    ComentarioDTO(
                        id=row[0],
                        id_barbero=row[1],
                        cliente_nombre=row[2],
                        contenido=row[3],
                        calificacion=row[4],
                        fecha_creacion=row[5]
                    ) for row in rows
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
                cursor.execute("""SELECT id, id_barbero, cliente_nombre, contenido, calificacion, fecha_creacion
                                  FROM comentarios WHERE id = %s""", (id,))
                row = cursor.fetchone()
                if row:
                    return ComentarioDTO(
                        id=row[0],
                        id_barbero=row[1],
                        cliente_nombre=row[2],
                        contenido=row[3],
                        calificacion=row[4],
                        fecha_creacion=row[5]
                    )
                return None
        except Exception as e:
            print(f"[ERROR] obtener_por_id(): {e}")
            raise
        finally:
            conn.close()

    def actualizar(self, comentario_dto):
        conn = ConexionDB().obtener_conexion()
        try:
            with conn.cursor() as cursor:
                sql = """UPDATE comentarios 
                         SET id_barbero = %s, cliente_nombre = %s, contenido = %s, calificacion = %s
                         WHERE id = %s"""
                cursor.execute(sql, (
                    comentario_dto.id_barbero,
                    comentario_dto.cliente_nombre,
                    comentario_dto.contenido,
                    comentario_dto.calificacion,
                    comentario_dto.id
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
                cursor.execute("DELETE FROM comentarios WHERE id = %s", (id,))
            conn.commit()
        except Exception as e:
            print(f"[ERROR] eliminar(): {e}")
            conn.rollback()
            raise
        finally:
            conn.close()


# DAO para PostgreSQL: usa misma lógica de MySQL por ahora
class ComentarioDAOPostgres(ComentarioDAOMySQL):
    pass
