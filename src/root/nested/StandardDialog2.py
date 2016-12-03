'''
Created on Dec 3, 2016

@author: dan
'''

import Tkinter as Tk
import tkMessageBox 

def main():
    root = Tk.Tk()
    root.title("KeyPress1")
    
    if tkMessageBox.askyesno("Print", "Print this report?"):
        print "yes was selected"
    else:
        print "no was selected"
        
    if tkMessageBox.askretrycancel("Retry Box", "Should we retry this?"):
        print "okay, we will retry it"
    else:
        print "then we will not retry things"
    
    root.mainloop()

if __name__ == '__main__':
    main()