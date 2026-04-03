from pydantic import BaseModel, Field

class VolumeInput(BaseModel):
    sets: int = Field(..., gt=0, description="Tamamlanan set sayısı")
    reps: int = Field(..., gt=0, description="Set başına tekrar sayısı")
    weight: float = Field(..., gt=0, description="Kullanılan ağırlık (kg)")

class VolumeResponse(BaseModel):
    total_volume: float
    intensity_score: float  # Yeni ekledik: Kurumsallık detayda gizlidir!