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
    
def test_read_player_positive():
    response = client.get("/player/123e4567-e89b-12d3-a456-426614174000")

    assert response.status_code == 200

    data = response.json()

    assert data["uuid"] == "123e4567-e89b-12d3-a456-426614174000"
    assert data["username"] == "MineCrafter_99"
    assert data["coins"] == 1550

def test_read_player_negative():
    response = client.get("/player/abc")

    assert response.status_code == 404

def test_update_player_stats_positive():
    response = client.post(
        "/player/update",
        json={
            "uuid": "123e4567-e89b-12d3-a456-426614174000",
            "stat_name": "coins",
            "value": 100
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert data["message"] == "Player statistics updated"
    assert data["stat_name"] == "coins"
    assert data["value"] == 100

def test_update_player_stats_invalid_uuid():
    response = client.post(
        "/player/update",
        json={
            "uuid": "abc",
            "stat_name": "coins",
            "value": 100
        }
    )

    assert response.status_code == 422

def test_update_player_stats_invalid_value():
    response = client.post(
        "/player/update",
        json={
            "uuid": "123e4567-e89b-12d3-a456-426614174000",
            "stat_name": "coins",
            "value": "abc"
        }
    )

    assert response.status_code == 422

def test_update_player_stats_missing_field():
    response = client.post(
        "/player/update",
        json={
            "uuid": "123e4567-e89b-12d3-a456-426614174000",
            "value": 100
        }
    )

    assert response.status_code == 422