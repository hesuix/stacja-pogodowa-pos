import random
from datetime import datetime

class SensorReader:
    """
    Klasa odpowiedzialna za symulację sprzętowych czujników stacji pogodowej.
    Zamiast odczytywać dane z pinów GPIO Raspberry Pi, generuje realistyczne 
    dane pogodowe w celu testowania reszty systemu.
    """

    def generate_mock_data(self) -> dict:
        """
        Generuje słownik z losowymi, ale realistycznymi danymi pogodowymi.
        
        Zwraca:
            dict: Słownik zawierający klucze: timestamp, temperature, 
                  pressure, wind_speed, precipitation.
        """
        return {
            'timestamp': datetime.now().isoformat(),
            'temperature': round(random.uniform(-20.0, 35.0), 1),
            'pressure': round(random.uniform(980.0, 1040.0), 1),
            'wind_speed': round(random.uniform(0.0, 120.0), 1),
            'precipitation': round(random.uniform(0.0, 50.0), 1)
        }
