from fastapi import APIRouter, HTTPException, Body
from modulos.Barberos.acceso_datos.get_factory import obtener_fabrica
from modulos.Barberos.acceso_datos.Barberos_dto import BarberoDTO

router = APIRouter()
dao = obtener_fabrica().crear_dao()

@router.post("/")
def crear_barbero(data: dict = Body(...)):
    try:
        barbero = BarberoDTO(
            nombre=data["nombre"],
            experiencia_anios=data.get("experiencia_anios", 0),
            especialidad=data.get("especialidad", ""),
            id_barberia=data["id_barberia"]
        )
        dao.guardar(barbero)
        return {"mensaje": "Barbero almacenado correctamente."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al guardar barbero: {e}")

@router.get("/")
def obtener_barberos():
    try:
        barberos = dao.obtener_todos()
        return [b.__dict__ for b in barberos]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener barberos: {e}")

@router.get("/{id}")
def obtener_barbero(id: int):
    try:
        barbero = dao.obtener_por_id(id)
        if not barbero:
            raise HTTPException(status_code=404, detail="Barbero no encontrado")
        return barbero.__dict__
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al buscar barbero: {e}")

@router.put("/{id}")
def actualizar_barbero(id: int, data: dict = Body(...)):
    try:
        actualizado = BarberoDTO(
            id=id,
            nombre=data["nombre"],
            experiencia_anios=data.get("experiencia_anios", 0),
            especialidad=data.get("especialidad", ""),
            id_barberia=data["id_barberia"]
        )
        dao.actualizar(actualizado)
        return {"mensaje": "Barbero actualizado correctamente."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar barbero: {e}")

@router.delete("/{id}")
def eliminar_barbero(id: int):
    try:
        dao.eliminar(id)
        return {"mensaje": "Barbero eliminado correctamente."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar barbero: {e}")
