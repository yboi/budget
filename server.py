import shutil
from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
from sqlalchemy.orm import sessionmaker
from models import User
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from urllib.parse import parse_qs
from config import db_name

# localhost:8000/register.html
Session = sessionmaker(bind=create_engine(f"sqlite:///{db_name}"))


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        """Serve a GET request."""
        if self.path == "/register.html":
            with open("register.html", "rb") as f:
                self.send_response(200)
                self.end_headers()
                shutil.copyfileobj(f, self.wfile)

    def do_POST(self):
        """Handle a POST request."""
        if self.path == "/register.html":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            parsed_data = parse_qs(post_data.decode())
            # Process the post_data
            with Session() as session:
                new_user = User(
                    login=parsed_data["login"][0],
                    user_name=parsed_data["user_name"][0],
                    email=parsed_data["email"][0],
                    password=parsed_data["password"][0]
                )
            session.add(new_user)
            session.commit()
            self.send_response(301)
            self.send_header("Location", "/login.html")
            self.end_headers()


server = HTTPServer(("", 8000), Handler)
server.serve_forever()
