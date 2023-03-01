#!/usr/bin/env python3
"""
Very simple HTTP server in python for logging requests
Usage::
    ./server.py [<port>]
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import os
import base64
import json


class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        logging.info(
            "GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers)
        )
        self._set_response()
        self.wfile.write("GET request for {}".format(self.path).encode("utf-8"))

    def do_POST(self):
        logging.info(
            "POST request,\nPath: %s\nHeaders:\n%s\n\n",
            str(self.path),
            str(self.headers),
        )
        content_length = int(
            self.headers["Content-Length"]
        )  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself

        if "multipart/form-data" in self.headers["Content-Type"]:
            boundary = self.headers["Content-Type"].split("boundary=")[1].encode()
            post_data = post_data.split(boundary)[1]
            header_bytes = post_data.split(b"\r\n")[1]

            if "filename=" in str(header_bytes):
                filename = str(header_bytes).split('filename="')[1].split('"')[0]
                body = post_data.split(b"\r\n\r\n")[1]
                file_path = os.path.join(os.getcwd(), filename)
                logging.info("Saving file to: %s\n", file_path)
                with open(file_path, "wb") as f:
                    f.write(body)

        else:
            logging.info("Body:\n%s\n", post_data.decode("utf-8"))
            # get json data from post request
            json_data = json.loads(post_data.decode("utf-8"))
            file_bytes = base64.b64decode(json_data["chart-file"])
            file_path = os.path.join(os.getcwd(), "chart2.png")
            logging.info("Saving file to: %s\n", file_path)
            with open(file_path, "wb") as f:
                f.write(file_bytes)

        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode("utf-8"))


def run(server_class=HTTPServer, handler_class=S, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    logging.info("Starting httpd...\n")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info("Stopping httpd...\n")


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
