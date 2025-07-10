from sqlalchemy.orm import Session
from app.models.sensor_model import Sensor
from app.schemas.sensor import SensorCreate
from sqlalchemy import func

# Obtener todos los sensores
def get_sensores(db: Session):
    return db.query(Sensor).all()

# Obtener un sensor por ID
def get_sensor(db: Session, sensor_id: int):
    return db.query(Sensor).filter(Sensor.id == sensor_id).first()

# Crear un nuevo sensor
def create_sensor(db: Session, sensor: SensorCreate):
    db_sensor = Sensor(**sensor.dict())
    db.add(db_sensor)
    db.commit()
    db.refresh(db_sensor)
    return db_sensor

# Listar solo sensores con valor mayor al umbral
def get_sensores_criticos(db: Session):
    sensores = db.query(Sensor).filter(Sensor.umbral_alarma != None).all()
    return [s for s in sensores if s.valor > s.umbral_alarma]

# Listar sensores con filtro por ubicación (opcional)
def get_sensores_filtrados(db: Session, ubicacion: str | None = None):
    query = db.query(Sensor)
    if ubicacion:
        query = query.filter(Sensor.ubicacion == ubicacion)
    return query.all()

def get_estadisticas(db: Session):
    total = db.query(func.count(Sensor.id)).scalar()
    media_valor = db.query(func.avg(Sensor.valor)).scalar() or 0.0

    sensores_criticos = [
        s for s in db.query(Sensor).filter(Sensor.umbral_alarma != None).all()
        if s.valor > s.umbral_alarma
    ]
    total_criticos = len(sensores_criticos)
    porcentaje_criticos = (total_criticos / total) * 100 if total else 0

    return {
        "total_sensores": total,
        "media_valor": round(media_valor, 2),
        "sensores_criticos": total_criticos,
        "porcentaje_criticos": round(porcentaje_criticos, 2)
    }