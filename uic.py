import tkinter as tk
import http.client
ip = input("server at :")
op = input("operation: ")
h1 = http.client.HTTPConnection(ip, port=8080)
master = tk.Tk() 
dispt = tk.StringVar()
view = tk.Label(master, textvariable=dispt).grid(row=0) 
tk.Label(master, text='Admission number').grid(row=1) 
tk.Label(master, text='Increment').grid(row=2) 
e1 = tk.Entry(master) 
e2 = tk.Entry(master)
def getit():
    adm = e1.get()
    inc = e2.get()
    incu = str(int(inc) + 10000)
    com = "/{}/{}/{}".format(op, incu, adm)
    h1.request("GET", com)
    d = h1.getresponse()
    data = d.read()
    rdat = str(data.decode('ascii'))
    dispt.set(rdat) 
b1 = tk.Button(master, text="Done", command=getit)
b1.grid(row=3, column=1)
e1.grid(row=1, column=1) 
e2.grid(row=2, column=1) 



        
tk.mainloop()