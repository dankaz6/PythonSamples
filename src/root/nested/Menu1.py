'''
Created on Sep 16, 2016

@author: kazsoft
'''

# http://effbot.org/tkinterbook/tkinter-application-windows.htm

from Tkinter import *

def callback():
    print "called the callback!"

root = Tk()
root.title("Menu1")

# create a menu
menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=callback)
filemenu.add_command(label="Open...", command=callback)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=callback)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=callback)

# add some text to the main screen
frame = Frame(root, width=200, height=200)
w = Label(frame, text="")
w.pack()
w = Label(frame, text="Hello, world! Hello Dan!")
w.pack()
w = Label(frame, text="")
w.pack()
frame.pack()

# create a status bar
status = Label(root, text="(status bar)", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

mainloop()