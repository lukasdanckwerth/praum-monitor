from http.server import HTTPServer, BaseHTTPRequestHandler
from http import HTTPStatus
from threading import Thread
import json
import csv


class _RequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(HTTPStatus.OK.value)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_GET(self):
        data = {
            "some": 12
        }
        with open("data/current_record.json", "r") as session_file:
            data = json.load(session_file)
            session_file.close()

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
    print("Start Server")

    httpd = HTTPServer(('', 1312), _RequestHandler, False)
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
