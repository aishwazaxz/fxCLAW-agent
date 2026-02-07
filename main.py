import http.server
import socketserver
import os

PORT = int(os.environ.get("PORT", 8080))

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"fxCLAW agent alive")

print("fxCLAW agent listening on port", PORT)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
