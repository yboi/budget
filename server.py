import http.server
import socketserver
import xml.etree.ElementTree as ET

# Read the users from the XML file
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

# Start the HTTP server
with socketserver.TCPServer(("", 8000), RequestHandler) as httpd:
    print("Serving at port", 8000)
    httpd.serve_forever()

