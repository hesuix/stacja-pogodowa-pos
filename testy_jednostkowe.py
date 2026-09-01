import pytest
from sensors import SensorReader

def test_sensor_temperature_range():
    """
    Test sprawdza, czy symulator czujnika generuje temperaturę
    w fizycznie możliwym zakresie dla warunków ziemskich.
    """
    # Arrange (Przygotowanie)
    reader = SensorReader()
    
    # Act (Działanie)
    data = reader.generate_mock_data()
    
    # Assert (Sprawdzenie)
    assert -40.0 <= data['temperature'] <= 60.0

def test_precipitation_cannot_be_negative():
    """
    Test sprawdza, czy poziom opadów nie przyjmuje wartości ujemnych
    (nie można mieć 'ujemnego' deszczu).
    """
    reader = SensorReader()
    data = reader.generate_mock_data()
    
    assert data['precipitation'] >= 0.0