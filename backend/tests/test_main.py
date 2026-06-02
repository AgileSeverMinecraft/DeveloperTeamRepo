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