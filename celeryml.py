import tasks
import http.server
from urllib.parse import urlparse
import re


class RequestHandler(http.server.BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        query = urlparse(self.path).query
        params = re.findall(r"[\d+.\d+']+", query)
        tasks.get_result.async(params)


server = http.server.HTTPServer(("localhost", 8080), RequestHandler)
try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
server.server_close()
