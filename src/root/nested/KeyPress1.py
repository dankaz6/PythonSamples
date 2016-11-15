'''
Created on Sep 16, 2016

@author: kazsoft
'''

# http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm


from Tkinter import *

root = Tk()
root.title("KeyPress1")

def key(event):
    print "pressed", repr(event.char)

def callback(event):
    frame.focus_set()
    print "clicked at", event.x, event.y

frame = Frame(root, width=200, height=200)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
w = Label(frame, text="Go ahead, click or press a key!")
w.bind("<Key>", key)
w.bind("<Button-1>", callback)
w.pack()
frame.pack()
root.mainloop()