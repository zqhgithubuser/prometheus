from prometheus_client import Gauge

INPROGRESS = Gauge("hello_worlds_inprogress", "Number of Hello Worlds in progress.")
LAST = Gauge("hello_world_last_time_seconds", "The last time a Hello World was served.")


class MyHandler(http.server.BaseHTTPRequestHandler):
    @INPROGRESS.track_inprogress()
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello World")
        LAST.set_to_current_time()
