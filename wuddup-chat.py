# Dvir Sadon
from Tkinter import *
import socket
import threading
import datetime

LABELX = 50
COUNTERY = 7


def trial():
    if str(e.get()) == "quit":
        client_socket.send(str(datetime.datetime.now())[11:16] + name)
        client_socket.send("has left the server")
        client_socket.close()
        top.destroy()
    else:
        client_socket.send(str(datetime.datetime.now())[11:16] + " " + name)
        # client_socket.send(name)  # padding maybe
        client_socket.send(e.get())
        frome = Label(top, text="You: " + e.get(), bg="lime green")
        global COUNTERY
        frome.place(x=LABELX, y=COUNTERY, anchor='c')
        COUNTERY += 20
        # new_lable.destroy()


def pgot():
    while True:
        print client_socket.recv(1024)


def loopit():
    top.mainloop()


name = ""


def stopfirst():
    if not str(got.get()).startswith("@"):
        global name
        name = got.get()
        first.destroy()


first = Tk()
first.geometry("200x90+300+300")  # width, hight, place(x,y)
namelable = Label(first, text="enter your name to continue")
namelable.place(x=100, y=7, anchor='c')
# my_lable = Label(top, text="wuddup?!", bg="red", fg="green")  # (bg=back, fg=text )color
# my_lable.pack(fill=X, padx=10, side=LEFT)  # fill the whole line
butt = Button(first, text="  continue  ", command=stopfirst)  # screen, text, when clicked whta to do
butt.place(relx=.65, rely=.7)
got = Entry(first)
got.place(relx=.01, rely=.7)
first.mainloop()

client_socket = socket.socket()
client_socket.connect(('127.0.0.1', 8478))

top = Tk()

# ##
top.geometry("250x200+300+300")  # width, hight, place(x,y)
new_lable = Label(top, text="Wuddup")
new_lable.place(x=120, y=7, anchor='c')
# my_lable = Label(top, text="wuddup?!", bg="red", fg="green")  # (bg=back, fg=text )color
# my_lable.pack(fill=X, padx=10, side=LEFT)  # fill the whole line
b = Button(top, text="  Send  ", command=trial)  # screen, text, when clicked whta to do
b.place(relx=.7, rely=.8)
e = Entry(top)
e.place(relx=.1, rely=.8)
# ##

thread = threading.Thread(target=loopit)
thread.start()
while True:  # 127
    # print client_socket.recv(1024)
    COUNTERY += 20
    if COUNTERY >= 127:
        COUNTERY = 27
    blanc = Label(top, text="                                    ")
    blanc.place(x=LABELX, y=COUNTERY, anchor='c')
    lb = Label(top, text=client_socket.recv(1024))
    lb.place(x=LABELX, y=COUNTERY, anchor='c')
