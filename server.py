from http.server import BaseHTTPRequestHandler, HTTPServer
import time

# When server is running, run ipconfig (ifconfig on UNIX) to get the IPv4 Address.
# Then go to http://<IPv4>:<hostPort>, for example http://192.168.1.102:8725
hostName = ""  # Or leave blank, i.e. hostName = ""
hostPort = 8725


class MyServer(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    # def do_GET(self):
    #     with open("index.html", "r+") as file:
    #         self._set_headers()
    #         self.wfile.write(bytes("<html><head><title>Spy Fall.</title></head>", "utf-8"))
    #         self.wfile.write(bytes("<body><p>This is a test</p>", "utf-8"))
    #         self.wfile.write(bytes("<p>You accessed path: {}</p>".format(self.path), "utf-8"))
    #         self.wfile.write(bytes("</body></html>", "utf-8"))

    def do_GET(self):
        with open("calculator.html", "r+") as file:
            m = file.read()

        self._set_headers()
        self.wfile.write(bytes(m,"utf-8"))
        self.wfile.write(bytes("<body><p> </p>", "utf-8"))
        self.wfile.write(bytes("<p> </p>".format(self.path), "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))





    def do_POST(self):
        # Doesn't do anything with posted data
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself
        print(post_data)
        self._set_headers()


if __name__ == '__main__':
    myServer = HTTPServer((hostName, hostPort), MyServer)
    print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

    try:
        myServer.serve_forever()
    except KeyboardInterrupt:
        pass

    myServer.server_close()
    print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))
