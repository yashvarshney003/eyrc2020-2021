import json
import tkinter

values = {}
root = tkinter.Tk()
kp = tkinter.DoubleVar()
ki = tkinter.DoubleVar()
kd = tkinter.DoubleVar()

def dmp(val):
    print('kp:', kp.get())
    print('ki:', ki.get())
    print('kd:', kd.get())
    values['kp']= [kp.get(), kp.get()]
    values['kd']= [kd.get(), kd.get()]
    values['ki']= [ki.get(), ki.get()]
    with open('data.json', 'w') as file:
        json.dump(values, file)
while True:
    kp = tkinter.Scale(root, from_ = 0, to = 1000, variable = kp, command = dmp)
    ki = tkinter.Scale(root, from_ = 0, to = 10, variable= ki, command = dmp)
    kd = tkinter.Scale(root, from_ = 0, to = 10, variable= kd, command = dmp)
    kp.pack()
    ki.pack()
    kd.pack()
    root.mainloop()
