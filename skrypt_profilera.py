import cProfile
import random
from db_manager import DatabaseManager

# Ustawiamy liczbę rekordów do zapisania (duża liczba pozwala zauważyć różnicę)
RECORDS_COUNT = 5000

def run_slow_unoptimized():
    """Symuluje awaryjny zapis 5000 rekordów (jedna po drugiej - wolno)."""
    db = DatabaseManager("slow_test.db")
    for _ in range(RECORDS_COUNT):
        temp = random.uniform(-10, 30)
        pressure = random.uniform(990, 1020)
        db.insert_record(temp, pressure)

def run_fast_optimized():
    """Symuluje awaryjny zapis 5000 rekordów (bulk insert - szybko)."""
    db = DatabaseManager("fast_test.db")
    # Generujemy listę danych z wyprzedzeniem
    records = [(random.uniform(-10, 30), random.uniform(990, 1020)) for _ in range(RECORDS_COUNT)]
    db.bulk_insert(records)

if __name__ == "__main__":
    print("\n=======================================================")
    print("--- PROFILOWANIE: WERSJA WOLNA (PRZED OPTYMALIZACJĄ) ---")
    print("Oczekiwany czas: ok. 1 - 3 sekundy. Czekaj...")
    print("=======================================================\n")
    
    # Uruchamiamy profiler dla wolnej funkcji i sortujemy po łącznym czasie
    cProfile.run('run_slow_unoptimized()', sort='cumtime')
    
    print("\n=======================================================")
    print("--- PROFILOWANIE: WERSJA SZYBKA (PO OPTYMALIZACJI) ---")
    print("Oczekiwany czas: ułamek sekundy.")
    print("=======================================================\n")
    
    # Uruchamiamy profiler dla zoptymalizowanej funkcji
    cProfile.run('run_fast_optimized()', sort='cumtime')