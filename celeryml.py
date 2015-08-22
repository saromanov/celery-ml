import tasks
import http.server
from urllib.parse import urlparse
import re

#Start to create server

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        query = urlparse(self.path).query
        params = re.findall(r"[\d+.\d+']+", query)
        result = tasks.get_result.delay(params)
        info = result.get()
        if info['error'] != '':
            tasks.compute_model.delay().get()
            return tasks.get_result.delay(params)
        else:
            return info


server = http.server.HTTPServer(("localhost", 8080), RequestHandler)
try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
server.server_close()
