from fastapi import FastAPI, HTTPException, Request
from datetime import datetime
import uvicorn
import uuid
import logging
from pydantic import BaseModel
from pathlib import Path
import json

STATS_FILE = Path("stats.json")


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

# Model danych do aktualizacji statystyk gracza
class PlayerStatUpdate(BaseModel):
    uuid: uuid.UUID
    stat_name: str
    value: int

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


@app.post("/player/update", status_code=201)
def update_player_stats(stat: PlayerStatUpdate):
    if STATS_FILE.exists():
        with open(STATS_FILE, "r") as f:
            stats = json.load(f)
    else:
        stats = {}

    player_id = str(stat.uuid)

    if player_id not in stats:
        stats[player_id] = {}

    stats[player_id][stat.stat_name] = stat.value

    with open(STATS_FILE, "w") as f:
        json.dump(stats, f, indent=4)

    return {
    "message": "Player statistics updated",
    "uuid": str(stat.uuid),
    "stat_name": stat.stat_name,
    "value": stat.value
}


# Uruchamiamy poleceniem:
# uv run uvicorn src.main:app --reload --no-access-log