from pydantic import BaseModel
from pydantic import ConfigDict
from datetime import datetime
from typing import Optional

# Base común para entrada y salida
class SensorBase(BaseModel):
    nombre: str
    ubicacion: str
    valor: float
    umbral_alarma: Optional[float] = None

# Esquema para creación (POST)
class SensorCreate(SensorBase):
    pass

# Esquema para lectura/salida
class SensorOut(SensorBase):
    id: int
    fecha: datetime
    estado_critico: bool = False

    model_config = ConfigDict(from_attributes=True)
