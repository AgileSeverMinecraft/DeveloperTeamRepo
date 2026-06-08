from fastapi import FastAPI, HTTPException, Request
from datetime import datetime
import uvicorn
import uuid
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s:\t%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Inicjalizacja aplikacji FastAPI
app = FastAPI(
    title="Minecraft Server API",
    description="API do zarządzania i monitorowania statusu serwera Minecraft."
)

# Middleware do logowania wszystkich żądań i odpowiedzi serwera
@app.middleware("http")
async def log_requests(request: Request, call_next):
    response = await call_next(request)

    logger.info(
        "%s %s %s",
        request.method,
        request.url.path,
        response.status_code,
    )

    return response

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
# uv run uvicorn src.main:app --reload --no-access-log