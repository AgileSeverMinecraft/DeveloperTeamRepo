# Minecraft Server Backend (DeveloperTeamRepo)

Projekt backendu pomocniczego dla serwera Minecraft realizowany w ramach przedmiotu dotyczącego metodologii Agile i Scrum.

## Stos Technologiczny & Architektura
* **Język:** Python 3.12+
* **Menedżer pakietów:** `uv` (Astral)
* **Framework WWW:** FastAPI (Asynchroniczne API)
* **Integracja z MC:** Protokół RCON (`mcrcon`) do zdalnego zarządzania serwerem gier.

Architektura opiera się na wzorcu usługowym (Service Layer). Kod źródłowy znajduje się w katalogu `src/`.
---

## Jak uruchomić projekt lokalnie?

Projekt wykorzystuje nowoczesne narzędzie `uv`. Nie musisz ręcznie tworzyć virtualenv ani instalować pip.

### 1. Wymagania wstępne
Upewnij się, że masz zainstalowane narzędzie `uv`. Jeśli go nie masz, zainstaluj jedną komendą:
* **Windows (PowerShell):** `irm https://astral.sh/uv/install.ps1 | iex`
* **macOS/Linux:** `curl -LsSf https://astral.sh/uv/install.sh | sh`

### 2. Instalacja zależności
Sklonuj repozytorium i wykonaj poniższe polecenie w folderze głównym. `uv` automatycznie stworzy środowisko i pobierze paczki:
```bash
uv sync