#!/usr/bin/env python3

from http import server
import socketserver
import threading
import json
from tools.tools import dump_data_to_file
import os


class SimpleHTTPRequestHandler(server.BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        content_len = int(self.headers.get_all('Content-Length')[0])
        # Read request content
        post_body = self.rfile.read(content_len)
        # Convert bytes to string
        tmp_str = post_body.decode('utf8').replace("'", '"')
        data = json.loads(tmp_str)
        # Save encoded request body
        dump_data_to_file(os.path.join(os.getcwd(), 'resources', 'data.txt'), "%s" % str(data["image"]))
        return


# HTTP server that can be started in background
class ThreadedHTTPServer(object):
    handler = SimpleHTTPRequestHandler

    def __init__(self, host, port):
        self.server = socketserver.TCPServer((host, port), self.handler)
        self.server_thread = threading.Thread(target=self.server.serve_forever)

    def start(self):
        self.server_thread.start()

    def is_alive(self):
        self.server_thread.is_alive()

    def stop(self):
        self.server.shutdown()
        self.server.server_close()