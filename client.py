import http.client
ip = input("server at :")
h1 = http.client.HTTPConnection(ip, port=8080)

ad = input("admission number :")
action = input("action :")
adj = input("adjust by :")
adju = str(int(adj)+10000)
com = "/{}/{}/{}".format(action, adju, ad)
h1.request("GET", com)
d = h1.getresponse()
data = d.read()
rdat = data.decode('ascii')
print(rdat)

