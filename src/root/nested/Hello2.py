'''
Created on Sep 16, 2016

@author: kazsoft
'''

from Tkinter import *

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print "hi there, everyone!"


def main():
    root = Tk()
    root.title("Hello2")

    app = App(root)
 
    root.mainloop()
    root.destroy() # optional; see description below



if __name__ == '__main__':
    main()
    
    