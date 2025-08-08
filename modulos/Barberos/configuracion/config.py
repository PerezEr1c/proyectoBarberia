import json

def cargar_configuracion(path="modulos/Barberos/configuracion/config.json"):
    with open(path) as f:
        return json.load(f)
