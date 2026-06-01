import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Servidor iniciado en el puerto {PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor stopped.")
        httpd.server_close()
