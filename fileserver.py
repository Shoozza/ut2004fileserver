import http.server
import socketserver
import socket
import os
from cfgparse import ConfigParser

PORT = 80
PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "system", "ut2004.ini")

Config = ConfigParser()
out = Config.add_file(PATH)
url = Config.add_option("RedirectToURL", dest='url', keys="IpDrv.HTTPDownload");
url.set("http://" + socket.gethostbyname(socket.gethostname()) + "/")
with open(PATH, "w", encoding='utf8') as ConfigFile:
        out.write(ConfigFile)

# serve files
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
httpd.serve_forever()
