from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Routers de cada módulo
from modulos.Comentarios.logica.Comentarios_service import router as comentarios_router
from modulos.Barberos.logica.Barberos_service import router as barberos_router
from modulos.Barberias.logica.Barberias_service import router as barberias_router  # ← Nuevo import

app = FastAPI(title="API Gateway")

# Middleware CORS para permitir peticiones desde frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],         # Permitir todos los orígenes (útil en desarrollo)
    allow_credentials=True,
    allow_methods=["*"],         # Permitir todos los métodos (GET, POST, PUT, DELETE)
    allow_headers=["*"]          # Permitir todos los headers
)

# Registrar routers
app.include_router(comentarios_router, prefix="/comentarios", tags=["Comentarios"])
app.include_router(barberos_router, prefix="/barberos", tags=["Barberos"])
app.include_router(barberias_router, prefix="/barberias", tags=["Barberías"])  # ← Nuevo registro
