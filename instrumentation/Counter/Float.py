import random

from prometheus_client import Counter

REQUESTS = Counter("hello_worlds_total", "Hello Worlds requested.")
SALES = Counter("hello_world_sales_euro_total", "Euros made serving Hello World.")


class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        REQUESTS.inc()
        euros = random.random()
        SALES.inc(euros)
        self.send_response(200)
        self.end_headers()
        self.wfile.write("Hello World for {} euros.".format(euros).encode())
