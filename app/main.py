from fastapi import FastAPI
from app.db.base import Base
from app.db.database import engine
from app.api.routes import router

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Instancia de la aplicación FastAPI
app = FastAPI(title="API de Gestión de Sensores Industriales")

# Incluir las rutas
app.include_router(router)
