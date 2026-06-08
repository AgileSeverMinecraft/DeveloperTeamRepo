from fastapi import FastAPI, HTTPException
from datetime import datetime
import uvicorn
import uuid

# Inicjalizacja aplikacji FastAPI
app = FastAPI(
    title="Minecraft Server API",
    description="API do zarządzania i monitorowania statusu serwera Minecraft."
)

# Endpoint główny zwracający JSON zgodnie z kryteriami akceptacji
@app.get("/")
def read_root():
    """
    Zwraca prostą wiadomość powitalną.
    """
    return {"message": "Hello World"}

# Nowy endpoint statusu
@app.get("/status")
def read_status():
    """
    Pobiera aktualny status serwera, wersję oraz znacznik czasu.
    """
    return {
        "status": "online",
        "version": "1.0.0",
        # Generujemy aktualny czas w formacie ISO (np. 2026-06-03T16:30:00.123456)
        "timestamp": datetime.now().isoformat()
    }

@app.get("/player/{uuid_str}")
def get_player_stats(uuid_str: str):
    # Walidacja formatu UUID
    try:
        uuid.UUID(uuid_str)
    except ValueError:
        # Jeśli format jest niepoprawny, zwracamy błąd 404
        raise HTTPException(status_code=404, detail="Invalid UUID format")
    
    # Zhardkodowane (mockowane) dane gracza
    return {
        "uuid": uuid_str,
        "username": "MineCrafter_99",
        "coins": 1550
    }
# Uruchamiamy poleceniem:
# uv run uvicorn src.main:app --reload
