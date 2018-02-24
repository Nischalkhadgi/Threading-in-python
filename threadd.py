from Tkinter import *
import tkMessageBox
import time
import threading

class form(object):
    def __init__(self,root):
        self.loopOn = True
        frame = Frame(root)
        frame.pack()

        redbutton = Button(frame, text="Loop On", fg="red", height = 5, width = 15, command = self.loopTurnOn)
        redbutton.pack(side=LEFT)

        redbutton2 = Button(frame, text="Loop Off", fg="blue", height=5, width=15, command=self.loopTurnOff)
        redbutton2.pack(side=LEFT)

    def printFuction(self):
        tkMessageBox.showinfo("Hello Python", "Hello World")

    def generateLoop(self):
        counter = 0
        self.loopOn = True
        while(self.loopOn):
            counter += 1
            print "Counter Value: "+ str(counter)
            time.sleep(1)

    def loopTurnOn(self):
        t = threading.Thread(target=self.generateLoop)
        t.start()

    def loopTurnOff(self):
        self.loopOn = False