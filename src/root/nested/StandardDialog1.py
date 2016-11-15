'''
Created on Sep 18, 2016

@author: kazsoft
'''

import Tkinter as Tk
import tkMessageBox 

def main():
    root = Tk.Tk()
    root.title("KeyPress1")
    
    def key(event):
        print "pressed", repr(event.char)
        tkMessageBox.showwarning("Key Pressed","Oh boy, key '{0}' was pressed!".format(event.char ))
        
    
    def callback(event):
        frame.focus_set()
        print "clicked at", event.x, event.y
        tkMessageBox.showinfo("Mouse Click", "You clicked the mouse at {0},{1}".format( event.x, event.y))
    
    print Tk.TkVersion
    frame = Tk.Frame(root, width=200, height=200)
    frame.bind("<Key>", key)
    frame.bind("<Button-1>", callback)
    w = Tk.Label(frame, text="Go ahead, click or press a key!")
    w.bind("<Key>", key)
    w.bind("<Button-1>", callback)
    w.pack()
    frame.pack()
    root.mainloop()


if __name__ == '__main__':
    main()