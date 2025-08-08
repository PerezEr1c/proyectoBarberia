import json
from fastapi import APIRouter, Request, HTTPException
from modulos.Barberias.acceso_datos.get_factory import obtener_fabrica_barberia
from modulos.Barberias.acceso_datos.Barberias_dto import BarberiaDTO

dao = obtener_fabrica_barberia().crear_dao()
router = APIRouter()

# Crear una barbería
@router.post("/")
async def crear_barberia(req: Request):
    data = await req.json()
    barberia = BarberiaDTO(
        nombre=data["nombre"],
        direccion=data.get("direccion"),
        telefono=data.get("telefono"),
        email=data.get("email")
    )
    dao.guardar(barberia)
    return {"mensaje": "Barbería almacenada correctamente."}


# Obtener todas las barberías
@router.get("/")
def obtener_barberias():
    barberias = dao.obtener_todos()
    return [b.__dict__ for b in barberias]


# Obtener una barbería por ID
@router.get("/{id}")
def obtener_barberia(id: int):
    barberia = dao.obtener_por_id(id)
    if not barberia:
        raise HTTPException(status_code=404, detail="Barbería no encontrada")
    return barberia.__dict__


# Actualizar una barbería por ID
@router.put("/{id}")
async def actualizar_barberia(id: int, req: Request):
    data = await req.json()
    actualizada = BarberiaDTO(
        id=id,
        nombre=data["nombre"],
        direccion=data.get("direccion"),
        telefono=data.get("telefono"),
        email=data.get("email")
    )
    dao.actualizar(actualizada)
    return {"mensaje": "Barbería actualizada correctamente."}


# Eliminar una barbería por ID
@router.delete("/{id}")
def eliminar_barberia(id: int):
    dao.eliminar(id)
    return {"mensaje": "Barbería eliminada correctamente."}
