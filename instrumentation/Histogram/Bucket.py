import http.server

from prometheus_client import Histogram, start_http_server

LATENCY = Histogram(
    "hello_world_latency_seconds",
    "Time for a request Hello World.",
    buckets=[0.0001, 0.0002, 0.0005, 0.001, 0.01, 0.1],
)


class MyHandler(http.server.BaseHTTPRequestHandler):
    @LATENCY.time()
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello World")


if __name__ == "__main__":
    start_http_server(8000)
    server = http.server.HTTPServer(("localhost", 8001), MyHandler)
    server.serve_forever()
