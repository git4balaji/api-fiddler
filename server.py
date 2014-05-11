#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
from parser import ObjectParser
import yaml
import os
import time

#Create custom HTTPRequestHandler class
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    
    #handle GET command
    def do_GET(self):
        rootdir = os.getcwd() + '/' #file location
        try:
            if self.path == '/':
                self.path = "/homepage.html"
                
            if self.path.endswith('.html'):
                f = open(rootdir + self.path) #open requested file

                #send code 200 response
                self.send_response(200)

                #send header first
                self.send_header('Content-type','text-html')
                self.end_headers()

                #send file content to client
                self.wfile.write(bytes(f.read(), 'UTF-8'))
                f.close()
                return
            else:
                self.yaml = yaml.load( open('outline.yaml', 'r') )
                self.parser = ObjectParser(self.yaml)
                
                json = self.parser.getData(self.path[1::])
                
                #send code 200 response
                self.send_response(200)

                #send header first
                self.send_header('Content-type','text-json')
                self.end_headers()

                #send file content to client
                self.wfile.write(bytes(json, 'UTF-8'))
                return
                      
        except IOError:
            self.send_error(404, 'Invalid Path')
    
def run():
    print('Http Server is starting...')
    
    #ip and port of servr
    #by default http server port is 8080
    HOST_NAME = '127.0.0.1'
    PORT_NUMBER = 8080
    
    server_address = (HOST_NAME, PORT_NUMBER)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(time.asctime(), ": Server Started - %s:%s" % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print();
    print(time.asctime(), ": Server Stopped - %s:%s" % (HOST_NAME, PORT_NUMBER))

if __name__ == '__main__':
    run()
