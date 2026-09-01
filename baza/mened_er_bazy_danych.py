import sqlite3

class DatabaseManager:
    """
    Klasa odpowiedzialna za zarządzanie połączeniem z relacyjną bazą danych SQLite
    oraz wykonywanie operacji zapisu pomiarów ze stacji pogodowej.
    """

    def __init__(self, db_path: str = "weather.db"):
        """
        Inicjalizuje menedżera bazy danych i tworzy tabele, jeśli nie istnieją.
        
        Args:
            db_path (str): Ścieżka do pliku bazy danych SQLite.
        """
        self.db_path = db_path
        self._initialize_db()

    def _initialize_db(self):
        """Metoda prywatna: tworzy tabelę 'measurements' w bazie."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS measurements (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    temp REAL,
                    pressure REAL
                )
            ''')
            conn.commit()

    def insert_record(self, temp: float, pressure: float):
        """
        Wersja NIEZOPTYMALIZOWANA (tzw. Wąskie Gardło / Hot Spot).
        Zapisuje pojedynczy pomiar, za każdym razem otwierając i zamykając 
        połączenie z bazą danych oraz wykonując commit.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO measurements (temp, pressure) VALUES (?, ?)", 
                (temp, pressure)
            )
            conn.commit()

    def bulk_insert(self, records: list):
        """
        Wersja ZOPTYMALIZOWANA.
        Wykorzystuje metodę 'executemany', aby zapisać tysiące rekordów 
        w ramach jednej transakcji i jednego połączenia z bazą.
        
        Args:
            records (list): Lista krotek zawierających dane (np. [(20.5, 1010.0), ...])
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.executemany(
                "INSERT INTO measurements (temp, pressure) VALUES (?, ?)", 
                records
            )
            conn.commit()
