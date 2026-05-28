import unittest
import urllib.request
import threading
from http.server import HTTPServer

# Importujemy handler i port z Twojego pliku main.py
from src.main import SimpleHandler, PORT


class TestSimpleServer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Uruchamiamy serwer przed wszystkimi testami w osobnym wątku (tzw. demonie)
        cls.server = HTTPServer(('localhost', PORT), SimpleHandler)
        cls.server_thread = threading.Thread(target=cls.server.serve_forever)
        cls.server_thread.daemon = True
        cls.server_thread.start()

    @classmethod
    def tearDownClass(cls):
        # Wyłączamy serwer po zakończeniu wszystkich testów
        cls.server.shutdown()
        cls.server.server_close()
        cls.server_thread.join()

    def test_hello_world_response(self):
        # Definiujemy adres, pod który uderzamy
        url = f"http://localhost:{PORT}/"

        # Wysyłamy żądanie GET
        with urllib.request.urlopen(url) as response:
            # 1. Sprawdzamy, czy serwer zwraca kod 200 OK
            self.assertEqual(response.status, 200)

            # 2. Odczytujemy i dekodujemy treść odpowiedzi
            body = response.read().decode('utf-8')

            # 3. Sprawdzamy poprawność komunikatu
            self.assertEqual(body, "Hello World")


if __name__ == "__main__":
    unittest.main()