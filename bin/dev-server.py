import http.server
import socketserver

PORT = 3000
DIRECTORY = "web-app/public"


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving " + DIRECTORY + " started at localhost:" + str(PORT))
    httpd.serve_forever()
