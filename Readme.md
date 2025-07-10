# Sensor Monitoring API

**Sensor Monitoring API** es un proyecto desarrollado con **FastAPI** que permite registrar, consultar y monitorizar sensores industriales.
---

## Funcionalidades

- Crear nuevos sensores con ubicación, valor y umbral de alarma.
- Consultar sensores por ID o filtrando por ubicación.
- Detectar sensores en estado crítico automáticamente (cuando el valor supera el umbral).
- Obtener estadísticas generales: número total, media, máximo y mínimo.
- Estructura modular: separación en carpetas `models/`, `schemas/`, `crud/`, `api/`, `db/`.

---

## Estructura del proyecto

```
.
├── app/
│   ├── api/
│   │   └── routes.py
│   ├── crud/
│   │   └── sensor_crud.py
│   ├── db/
│   │   ├── base.py
│   │   └── database.py
│   ├── models/
│   │   └── sensor_model.py
│   ├── schemas/
│   │   └── sensor.py
│   └── main.py
├── requirements.txt
└── README.md
```

---

## Cómo ejecutar el proyecto

1. **Clona el repositorio**

```bash
git clone
cd sensor-monitoring-api
```

2. **Crea un entorno virtual**

```bash
python -m venv venv
venv\Scripts\activate  # En Windows
source venv/bin/activate  # En Linux/Mac
```

3. **Instala dependencias**

```bash
pip install -r requirements.txt
```

4. **Ejecuta el servidor**

```bash
uvicorn app.main:app --reload
```

5. **Abre el navegador en**:  
   [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Endpoints destacados

| Método | Ruta                     | Descripción                            |
|--------|--------------------------|----------------------------------------|
| POST   | `/sensores/`             | Crea un nuevo sensor                   |
| GET    | `/sensores/`             | Lista sensores (opcional: ubicación)   |
| GET    | `/sensores/{id}`         | Obtiene un sensor por ID               |
| GET    | `/sensores/criticos`     | Lista solo los sensores críticos       |
| GET    | `/sensores/estadisticas` | Devuelve estadísticas generales        |

---

## Stack técnico

- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic v2](https://docs.pydantic.dev/latest/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [SQLite](https://www.sqlite.org/index.html)

---

## Autor

Creado por [Manuel A.G.](https://github.com/manugr1)

---

## Próximas mejoras

- Añadir autenticación y roles de usuario.
- Conectar con PostgreSQL en entorno productivo.
- Tests automáticos con `pytest`.


