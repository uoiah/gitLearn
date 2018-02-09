from tkinter import *

class App(Frame):

   def __init__(self, master = None):
      super.__init__(master)
      self.pack()

root = Tk()
root.geometry("640x480")
myapp = App(master = root)
myapp.mainloop()

