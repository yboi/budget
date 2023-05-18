import shutil
from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
from http.server import SimpleHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        """Serve a GET request."""
        f = open("index.html")
        if self.path == "/index.html":
            shutil.copyfileobj(f, self.wfile)
            f.close()

server = HTTPServer(("", 8000), Handler)
server.serve_forever()
#TODO add do_POST
