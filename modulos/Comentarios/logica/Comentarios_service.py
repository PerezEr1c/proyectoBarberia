from fastapi import APIRouter, HTTPException, Body
from modulos.Comentarios.acceso_datos.get_factory import obtener_fabrica
from modulos.Comentarios.acceso_datos.Comentarios_dto import ComentarioDTO

router = APIRouter()
dao = obtener_fabrica().crear_dao()

@router.post("/")
def crear_comentario(data: dict = Body(...)):
    try:
        comentario = ComentarioDTO(
            id_barbero=data["id_barbero"],
            cliente_nombre=data["cliente_nombre"],
            contenido=data["contenido"],
            calificacion=data["calificacion"],    
        )
        dao.guardar(comentario)
        return {"mensaje": "Comentario almacenado correctamente."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al guardar comentario: {e}")

@router.get("/")
def obtener_comentarios():
    try:
        comentarios = dao.obtener_todos()
        return [c.__dict__ for c in comentarios]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener comentarios: {e}")

@router.get("/{id}")
def obtener_comentario(id: int):
    try:
        comentario = dao.obtener_por_id(id)
        if not comentario:
            raise HTTPException(status_code=404, detail="Comentario no encontrado")
        return comentario.__dict__
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al buscar comentario: {e}")

@router.put("/{id}")
def actualizar_comentario(id: int, data: dict = Body(...)):
    try:
        actualizado = ComentarioDTO(
            id=id,
            id_barbero=data["id_barbero"],
            cliente_nombre=data["cliente_nombre"],
            contenido=data["contenido"],
            calificacion=data["calificacion"],  
        )
        dao.actualizar(actualizado)
        return {"mensaje": "Comentario actualizado correctamente."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar comentario: {e}")

@router.delete("/{id}")
def eliminar_comentario(id: int):
    try:
        dao.eliminar(id)
        return {"mensaje": "Comentario eliminado correctamente."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar comentario: {e}")
