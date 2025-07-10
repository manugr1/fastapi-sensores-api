from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.schemas.sensor import SensorCreate, SensorOut
from app.crud import sensor_crud

router = APIRouter()

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/sensores/")
def crear_sensor(sensor: SensorCreate, db: Session = Depends(get_db)):
    sensor_creado = sensor_crud.create_sensor(db, sensor)
    return SensorOut.from_orm(sensor_creado).copy(update={
        "estado_critico": (
            sensor_creado.umbral_alarma is not None and sensor_creado.valor > sensor_creado.umbral_alarma
        )
    })




@router.get("/sensores/")
def listar_sensores(ubicacion: str | None = None, db: Session = Depends(get_db)):
    sensores = sensor_crud.get_sensores_filtrados(db, ubicacion)
    return [
        SensorOut.from_orm(sensor).copy(update={
            "estado_critico": (
                sensor.umbral_alarma is not None and sensor.valor > sensor.umbral_alarma
            )
        })
        for sensor in sensores
    ]

@router.get("/sensores/criticos", response_model=list[SensorOut])
def sensores_criticos(db: Session = Depends(get_db)):
    sensores = sensor_crud.get_sensores_criticos(db)
    return [
        SensorOut.from_orm(sensor).copy(update={"estado_critico": True})
        for sensor in sensores
    ]


@router.get("/sensores/estadisticas")
def obtener_estadisticas(db: Session = Depends(get_db)):
    return sensor_crud.get_estadisticas(db)


@router.get("/sensores/{sensor_id}")
def obtener_sensor(sensor_id: int, db: Session = Depends(get_db)):
    sensor = sensor_crud.get_sensor(db, sensor_id)
    if not sensor:
        raise HTTPException(status_code=404, detail="Sensor no encontrado")
    return SensorOut.from_orm(sensor).copy(update={
        "estado_critico": (
            sensor.umbral_alarma is not None and sensor.valor > sensor.umbral_alarma
        )
    })
