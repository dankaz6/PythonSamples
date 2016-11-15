'''
Created on Sep 16, 2016

@author: kazsoft
'''

from Tkinter import *

root = Tk()
root.title("MouseClick1")

def callback(event):
    print "clicked at", event.x, event.y

frame = Frame(root, width=100, height=100)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()