from http.server import HTTPServer, BaseHTTPRequestHandler

# Numer portu: 8000
PORT = 8000

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        # Treść odpowiedzi
        self.wfile.write(b"Hello World")

def run():
    server_address = ('localhost', PORT)
    httpd = HTTPServer(server_address, SimpleHandler)
    print(f"Serwer startuje na http://localhost:{PORT}")
    httpd.serve_forever()
    # Odpowiedz - curl http://localhost:8000

if __name__ == "__main__":
    run()
