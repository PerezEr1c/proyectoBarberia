import json
import pymysql
import psycopg2

class ConexionDB:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._cargar_configuracion()
        return cls._instancia

    def _cargar_configuracion(self):
        with open("modulos/Comentarios/configuracion/config.json") as f:
            config = json.load(f)
        self.config_general = config
        self.motor = config["db_engine"]
        self.db_config = config[self.motor]

    def _crear_conexion(self):
        if self.motor == "mysql":
            return pymysql.connect(
                host=self.db_config["host"],
                port=self.db_config["port"],
                user=self.db_config["user"],
                password=self.db_config["password"],
                database=self.db_config["database"],
                cursorclass=pymysql.cursors.Cursor
            )
        elif self.motor == "postgres":
            return psycopg2.connect(
                host=self.db_config["host"],
                port=self.db_config["port"],
                user=self.db_config["user"],
                password=self.db_config["password"],
                dbname=self.db_config["database"]
            )
        else:
            raise ValueError(f"Motor de base de datos no soportado: {self.motor}")

    def obtener_conexion(self):
        try:
            return self._crear_conexion()
        except Exception as e:
            print(f"[ERROR] al obtener conexión: {e}")
            raise
