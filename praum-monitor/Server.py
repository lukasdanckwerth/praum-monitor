from http.server import HTTPServer, BaseHTTPRequestHandler
from http import HTTPStatus
from threading import Thread
import json

# Sample blog post data similar to
# https://ordina-jworks.github.io/frontend/2019/03/04/vue-with-typescript.html#4-how-to-write-your-first-component
_g_posts = [
    {
        'title': 'My first blogpost ever!',
        'body': 'Lorem ipsum dolor sit amet.',
        'author': 'Elke',
        'date_ms': 1593607500000,  # 2020 July 1 8:45 AM Eastern
    },
    {
        'title': 'Look I am blogging!',
        'body': 'Hurray for me, this is my second post!',
        'author': 'Elke',
        'date_ms': 1593870300000,  # 2020 July 4 9:45 AM Eastern
    },
    {
        'title': 'Another one?!',
        'body': 'Another one!',
        'author': 'Elke',
        'date_ms': 1594419000000,  # 2020 July 10 18:10 Eastern
    }
]


class _RequestHandler(BaseHTTPRequestHandler):
    # Borrowing from https://gist.github.com/nitaku/10d0662536f37a087e1b
    def _set_headers(self):
        self.send_response(HTTPStatus.OK.value)
        self.send_header('Content-type', 'application/json')
        # Allow requests from any origin, so CORS policies don't
        # prevent local development.
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_GET(self):
        data = {
            "some": 12
        }
        self._set_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))

    def do_OPTIONS(self):
        # Send allow-origin header for preflight POST XHRs.
        self.send_response(HTTPStatus.NO_CONTENT.value)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('Access-Control-Allow-Headers', 'content-type')
        self.end_headers()


def run_server():
    print("Initializing server")

    httpd = HTTPServer(('', 8001), _RequestHandler, False)
    httpd.server_bind()
    httpd.server_activate()

    print('Serving at %s:%d' % httpd.server_address)

    def serve_forever(httpd):
        with httpd:  # to make sure httpd.server_close is called
            print("Server will server forever\n")
            httpd.serve_forever()
            print("Server left infinite request loop")

    thread = Thread(target=serve_forever, args=(httpd,))
    thread.setDaemon(True)
    thread.start()


if __name__ == '__main__':
    run_server()
