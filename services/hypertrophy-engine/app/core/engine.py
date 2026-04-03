class WorkoutEngine:
    @staticmethod
    def calculate_total_volume(sets: int, reps: int, weight: float) -> float:
        return sets * reps * weight

    @staticmethod
    def calculate_intensity(weight: float, reps: int) -> float:
        # Basit bir yoğunluk skoru algoritması
        return (weight * reps) / 100