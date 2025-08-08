import json

def cargar_configuracion():
    with open("modulos/Barberias/configuracion/config.json") as archivo:
        configuracion = json.load(archivo)
    return configuracion
