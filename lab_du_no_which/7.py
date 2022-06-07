from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 3000


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.responses == 404:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>Test</title></head>", "utf-8"))
            self.wfile.write(bytes(f"<p>Request: {hostName}:{serverPort}{self.path}</p>", "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes(f"<p>An error has occured. Error: {self.responses}</p>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>Test</title></head>", "utf-8"))
            self.wfile.write(bytes(f"<p>Request: {hostName}:{serverPort}{self.path}</p>", "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
            self.wfile.write(bytes("<a href='/another'>Go to another page</a>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))
        elif self.path == '/another':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>Another</title></head>", "utf-8"))
            self.wfile.write(bytes(f"<p>Request: {hostName}:{serverPort}{self.path}</p>", "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes("<p>This is an example of another page</p>", "utf-8"))
            self.wfile.write(bytes("<a href='/'>Go back</a>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started http://{hostName}:{serverPort}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
