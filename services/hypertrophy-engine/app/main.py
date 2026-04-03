from fastapi import FastAPI
from app.schemas import VolumeInput, VolumeResponse
from app.core.engine import WorkoutEngine

app = FastAPI(title="Olympos Hypertrophy Engine", version="1.0.4")

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "hypertrophy-engine"}

@app.post("/calculate-volume", response_model=VolumeResponse)
def calculate_volume(data: VolumeInput):
    volume = WorkoutEngine.calculate_total_volume(data.sets, data.reps, data.weight)
    intensity = WorkoutEngine.calculate_intensity(data.weight, data.reps)
    return {"total_volume": volume, "intensity_score": intensity}