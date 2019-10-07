from http.server import BaseHTTPRequestHandler, HTTPServer
import numpy
ip = ""
class Serv(BaseHTTPRequestHandler):
    dic = numpy.zeros((1600, 3))
    i = 0
    while i < 1600:
        dic[i][0] = i
        i = i + 1
        
    print("Input address")
    ip = input()
    def do_GET(self):
        
        request = self.path
        action = request[1:2]
        val = int(request[3:8]) - 10000
        addr = int(request[9:])
        resp = ""
        if action == "p":
            try:
                resp = str(self.dic[addr][1])
            except KeyError:
                resp = "Invalid User ID"
        elif action == "i":
            try:
                bal = self.dic[addr][1]
                bal += val
                self.dic[addr][1] = bal
                resp = str(self.dic[addr][1])
            except KeyError:
                resp = "Invalid User ID"
        elif action == "d":
            try:
                bal = self.dic[addr][1]
                if (bal - val ) > -1:
                    bal -= val
                    self.dic[addr][1] = bal
                    resp = str(self.dic[addr][1])
                else:
                    resp = "insufficient balance"
            except KeyError:
                resp = "Invalid User ID"
        elif action == "q":
            try:
                self.dic[addr][2] += val
                resp = str(self.dic[addr][2])
            except KeyError:
                resp = "Invalid User ID"
        else:
            resp = "Fatal error. Invalid request. Contact admin"
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes(resp, 'utf-8'))
        
httpd = HTTPServer((ip, 8080) , Serv)
httpd.serve_forever()
