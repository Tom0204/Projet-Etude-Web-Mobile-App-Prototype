from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import sensors, weather
from services.data_init import initialize_data_files

app = FastAPI(
    title="AgriSense API",
    description="Back-end pour l'application d'aide aux agriculteurs",
    version="1.0.0"
)

# Lien avec front en production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialisation CSV
@app.on_event("startup")
def on_startup():
    initialize_data_files()

# Routers
app.include_router(sensors.router, prefix="/sensors", tags=["Capteurs"])
app.include_router(weather.router, prefix="/weather", tags=["Météo"])

@app.get("/", tags=["Santé"])
def health_check():
    return {"status": "ok", "message": "AgriSense API opérationnelle"}
