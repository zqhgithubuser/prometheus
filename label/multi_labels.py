import http.server

from prometheus_client import Counter, start_http_server

REQUESTS = Counter(
    "hello_worlds_total", "Hello Worlds requested.", labelnames=["path", "method"]
)


class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        REQUESTS.labels(self.path, self.command).inc()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello World")


if __name__ == "__main__":
    start_http_server(8000)
    server = http.server.HTTPServer(("localhost", 8001), MyHandler)
    server.serve_forever()
