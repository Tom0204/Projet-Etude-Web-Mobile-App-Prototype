from pydantic import BaseModel, Field
from typing import Optional, Literal


class WeatherInput(BaseModel):
    station_id: str = Field(..., example="W001", description="Identifiant de la station météo")
    rain_mm: float = Field(..., ge=0, example=5.2, description="Précipitations en mm")
    wind_speed_kmh: float = Field(..., ge=0, example=18.0, description="Vitesse du vent en km/h")
    wind_direction: str = Field(..., example="NO", description="Direction du vent (N, NE, E, SE, S, SO, O, NO)")
    sunshine_hours: float = Field(..., ge=0, le=24, example=7.5, description="Heures d'ensoleillement")
    uv_index: float = Field(..., ge=0, le=11, example=4.2, description="Indice UV")
    timestamp: Optional[str] = Field(None, description="Timestamp ISO (auto-généré si absent)")

    model_config = {"json_schema_extra": {"example": {
        "station_id": "W001",
        "rain_mm": 5.2,
        "wind_speed_kmh": 18.0,
        "wind_direction": "NO",
        "sunshine_hours": 7.5,
        "uv_index": 4.2,
    }}}
