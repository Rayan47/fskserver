from http.server import BaseHTTPRequestHandler, HTTPServer
ip = ""
class Serv(BaseHTTPRequestHandler):
    dic = {}
    i = 0
    while(i < 1600):
            dic[str(i)] = str(0)
            i = i + 1
    print("initf")
    print("Input address")
    ip = input()
    if ip == "d":
        ip = "13.235.75.0"
    def do_GET(self):
        
        request = self.path
        action = request[1:2]
        addr = request[3:]
        resp = ""
        if action == "p":
            try:
                resp = self.dic[addr]
            except KeyError:
                resp = "Invalid User ID"
        elif action == "i":
            try:
                bal = int(self.dic[addr])
                bal += 1
                self.dic[addr] = str(bal)
                resp = self.dic[addr]
            except KeyError:
                resp = "Invalid User ID"
        elif action == "d":
            try:
                bal = int(self.dic[addr])
                if (bal - 1) > -1:
                    bal -= 1
                    self.dic[addr] = str(bal)
                    resp = self.dic[addr]
                else:
                    resp = "insufficient balance"
            except KeyError:
                resp = "Invalid User ID"
        else:
            resp = "Fatal error. Invalid request. Contact admin"
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes(resp, 'utf-8'))
        
httpd = HTTPServer((ip, 8080) , Serv)
httpd.serve_forever()