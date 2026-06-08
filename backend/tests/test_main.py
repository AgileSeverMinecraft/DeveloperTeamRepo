from fastapi.testclient import TestClient

# Importujemy naszą aplikację z folderu src
from src.main import app

# Tworzymy klienta testowego
client = TestClient(app)


def test_read_root():
    # Wykonanie żądania GET do endpointa "/"
    response = client.get("/")

    # 1. Sprawdzenie, czy serwer odpowiada kodem 200 (OK)
    assert response.status_code == 200

    # 2. Sprawdzenie, czy odpowiedź to wymagany JSON
    assert response.json() == {"message": "Hello World"}

# Nowy test dla endpointa /status
def test_read_status():
    response = client.get("/status")

    # 1. Sprawdzenie, czy serwer odpowiada kodem 200 (OK)
    assert response.status_code == 200

    # 2. Pobranie danych JSON z odpowiedzi
    data = response.json()

    # 3. Weryfikacja poszczególnych pól z kryteriów akceptacji
    assert data["status"] == "online"
    assert data["version"] == "1.0.0"

    # 4. Sprawdzenie, czy klucz timestamp w ogóle istnieje w odpowiedzi
    assert "timestamp" in data

# Test dla dokumentacji Swagger UI
def test_swagger_ui():
    response = client.get("/docs")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]