from fastapi import APIRouter, Query, HTTPException
from typing import Optional
from services.csv_reader import read_csv, filter_rows, select_fields, paginate, apply_date_filter
from services.csv_writer import append_row, inject_timestamp
from models.sensor_models import SensorInput

router = APIRouter()

SENSOR_FILE = "sensors.csv"

ALL_FIELDS = ["timestamp", "sensor_id", "temperature_c", "humidity_pct", "soil_moisture_pct", "soil_ph"]


def _get_sensor_data(
    sensor_id: Optional[str],
    date_from: Optional[str],
    date_to: Optional[str],
    fields: Optional[list[str]],
    limit: int,
    offset: int,
) -> list[dict]:
    rows = read_csv(SENSOR_FILE)
    rows = filter_rows(rows, {"sensor_id": sensor_id})
    rows = apply_date_filter(rows, date_from, date_to)
    rows = select_fields(rows, fields)
    return paginate(rows, limit, offset)


@router.get("/")
def get_all_sensor_data(
    sensor_id: Optional[str] = Query(None, description="Filtrer par capteur (ex: S001)"),
    fields: Optional[str] = Query(None, description="Colonnes souhaitées séparées par virgule (ex: timestamp,temperature_c)"),
    date_from: Optional[str] = Query(None, description="Date de début ISO (ex: 2024-01-01)"),
    date_to: Optional[str] = Query(None, description="Date de fin ISO (ex: 2024-12-31)"),
    limit: int = Query(50, ge=1, le=1000),
    offset: int = Query(0, ge=0),
):
    field_list = [f.strip() for f in fields.split(",")] if fields else None
    if field_list:
        invalid = [f for f in field_list if f not in ALL_FIELDS]
        if invalid:
            raise HTTPException(status_code=400, detail=f"Champs invalides : {invalid}. Disponibles : {ALL_FIELDS}")
    return _get_sensor_data(sensor_id, date_from, date_to, field_list, limit, offset)


@router.get("/temperature")
def get_temperature(
    sensor_id: Optional[str] = Query(None),
    date_from: Optional[str] = Query(None),
    date_to: Optional[str] = Query(None),
    limit: int = Query(50, ge=1, le=1000),
    offset: int = Query(0, ge=0),
):
    return _get_sensor_data(sensor_id, date_from, date_to, ["timestamp", "sensor_id", "temperature_c"], limit, offset)


@router.get("/humidity")
def get_humidity(
    sensor_id: Optional[str] = Query(None),
    date_from: Optional[str] = Query(None),
    date_to: Optional[str] = Query(None),
    limit: int = Query(50, ge=1, le=1000),
    offset: int = Query(0, ge=0),
):
    return _get_sensor_data(sensor_id, date_from, date_to, ["timestamp", "sensor_id", "humidity_pct"], limit, offset)


@router.get("/soil")
def get_soil(
    sensor_id: Optional[str] = Query(None),
    date_from: Optional[str] = Query(None),
    date_to: Optional[str] = Query(None),
    limit: int = Query(50, ge=1, le=1000),
    offset: int = Query(0, ge=0),
):
    return _get_sensor_data(sensor_id, date_from, date_to, ["timestamp", "sensor_id", "soil_moisture_pct", "soil_ph"], limit, offset)


@router.get("/latest")
def get_latest(sensor_id: Optional[str] = Query(None)):
    rows = read_csv(SENSOR_FILE)
    rows = filter_rows(rows, {"sensor_id": sensor_id})
    if not rows:
        raise HTTPException(status_code=404, detail="Aucune donnée trouvée.")
    return rows[-1]


@router.get("/sensors-list")
def list_sensors():
    rows = read_csv(SENSOR_FILE)
    ids = sorted(set(r["sensor_id"] for r in rows if r.get("sensor_id")))
    return {"sensor_ids": ids}


@router.post("/", status_code=201)
def add_sensor_reading(data: SensorInput):
    row = inject_timestamp(data.model_dump())
    append_row(SENSOR_FILE, row)
    return {"status": "created", "data": row}
