from fastapi import FastAPI
import uvicorn

# Inicjalizacja aplikacji FastAPI
app = FastAPI(title="Minecraft Server API")

# Endpoint główny zwracający JSON zgodnie z kryteriami akceptacji
@app.get("/")
def read_root():
    return {"message": "Hello World"}

# Uruchamiamy poleceniem:
# uv run uvicorn src.main:app --reload