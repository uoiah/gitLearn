from tkinter import *

class App(Frame):
  
  def __init__(self, master = None):
    super().__init__(master)
    self.pack()

    self.entry1 = Entry()
    self.entry1.pack(side = "top")

    self.okbtn = Button()
    self.okbtn["text"] = "ok"
    self.okbtn["command"] = self.prtsth
    self.okbtn.pack(side = "top", expand = 1)
    self.resetbtn = Button()
    self.resetbtn["text"] = "reset"
    self.resetbtn["command"] = self.clssth
    self.resetbtn.pack(side = "top")
    
    self.contents1 = StringVar()
    self.contents1.set("2000")
    
    self.entry1["textvariable"] = self.contents1

    #self.entry1.bind('<Key-Return>', self.prtsth)

  def clssth(self):
    self.contents1.set("")
    

  def prtsth(self):
    yearstr = self.contents1.get()
    year = int(yearstr)
    if year % 400 == 0:
      self.contents1.set(yearstr + " is leaf year.")
    elif year % 100 == 0:
      self.contents1.set(yearstr + " is not leaf year.")
    elif year % 4 == 0:
      self.contents1.set(yearstr + " is leaf year.")
    else:
      self.contents1.set(yearstr + " is not leaf year.")
    #self.entry["textvariable"] = yearstr
    print("what's in Entry is:", yearstr)

root = Tk()
root.title('leafyear')
root.geometry('640x480')
myapp = App(master = root)
myapp.mainloop()
