from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.db.base import Base

class Sensor(Base):
    __tablename__ = "sensores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    ubicacion = Column(String)
    valor = Column(Float)
    fecha = Column(DateTime, default=datetime.utcnow)
    
    umbral_alarma = Column(Float, nullable=True)
