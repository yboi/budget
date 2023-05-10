import http.server
import socketserver
import xml.etree.ElementTree as ET
from flask import Flask
import database
# from database import register_user


# create the Flask application instance
app = Flask(__name__)
# http://localhost:8000/login.html
# Read the users from the XML file
# TODO SQLite with SQLAlechemy for data. Work on a database schema and then implement it. SQLAlchemy: https://docs.sqlalchemy.org/en/20
tree = ET.parse('users.xml')
users = tree.findall('user')

# Define the request handler for the HTTP server
class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        # Get the username and password from the form data
        content_length = int(self.headers['Content-Length'])
        form_data = self.rfile.read(content_length).decode('utf-8')
        username = form_data.split('&')[0].split('=')[1]
        password = form_data.split('&')[1].split('=')[1]

        # Check if the username and password are valid
        for user in users:
            if user.attrib['username'] == username and user.attrib['password'] == password:
                # If the username and password are valid, set the response message to "Login success"
                message = "Login success"
                # TODO here must be redirect to home page
                break
        else:
            # If the username and password are not valid, set the response message to "Invalid username or password"
            message = "Invalid username or password"

        # Fill in the message in the login.html template and send the response
        with open('login.html', 'rb') as f:
            template = f.read().decode('utf-8')
            template = template.replace('{{ message }}', message)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(template.encode('utf-8'))

    @app.route('/register', methods=['POST'])
    def register(self):
        # Get the username and password from the form data
        content_length = int(self.headers['Content-Length'])
        form_data = self.rfile.read(content_length).decode('utf-8')

        username = form_data.split('&')[0].split('=')[1]
        password = form_data.split('&')[1].split('=')[1]
        email = form_data.split('&')[2].split('=')[1]

        # Check if the username already exists
        for user in users:
            if user.attrib['username'] == username:
                message = "Username already exists"
                break
        else:
            # If the username does not exist, create a new user element and append it to the root element
            new_user = ET.Element('user')
            # new_user.attrib['username'] = username
            # new_user.attrib['password'] = password
            database.register_user(username, password, email)
            # tree.getroot().append(new_user)
            # tree.write('users.xml')
            return redirect('/success')

        # Fill in the message in the register.html template and send the response
        with open('register.html', 'rb') as f:
            template = f.read().decode('utf-8')
            template = template.replace('{{ message }}', message)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(template.encode('utf-8'))

    def display_forgot_page(self):
        with open('forgot.html', 'rb') as f:
            template = f.read().decode('utf-8')
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(template.encode('utf-8'))


# Start the HTTP server
with socketserver.TCPServer(("", 8000), RequestHandler) as httpd:
    print("Serving at port", 8000)
    httpd.serve_forever()

