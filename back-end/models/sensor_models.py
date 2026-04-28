from pydantic import BaseModel, Field
from typing import Optional


class SensorInput(BaseModel):
    sensor_id: str = Field(..., example="S001", description="Identifiant du capteur")
    temperature_c: float = Field(..., example=22.5, description="Température en °C")
    humidity_pct: float = Field(..., ge=0, le=100, example=65.0, description="Humidité air en %")
    soil_moisture_pct: float = Field(..., ge=0, le=100, example=42.0, description="Humidité sol en %")
    soil_ph: float = Field(..., ge=0, le=14, example=6.8, description="pH du sol")
    timestamp: Optional[str] = Field(None, description="Timestamp ISO (auto-généré si absent)")

    model_config = {"json_schema_extra": {"example": {
        "sensor_id": "S001",
        "temperature_c": 22.5,
        "humidity_pct": 65.0,
        "soil_moisture_pct": 42.0,
        "soil_ph": 6.8,
    }}}
