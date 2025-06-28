"""Smth about imports."""
import http.server
import socketserver

PORT=8000


class TestMe():
    """Test class."""
    def take_five(self):
        """Function returns 5."""
        return 5
    def port(self):
        """Function returns PORT."""
        return PORT

if __name__ == '__main__':
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as http:
        print("serving at port", PORT)
        http.serve_forever()
