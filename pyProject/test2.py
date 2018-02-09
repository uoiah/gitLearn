# -*- coding:UTF-8 -*-

from tkinter import *

class LeafYear(Frame):


  def __init__(self, master = None):
    super().__init__(master)
    self.pack()
    self.create_widgets()
  
  def create_widgets(self):
    self.okbtn = Button(self)
    self.okbtn["text"] = "确定"
    self.okbtn["command"] = self.judge()
    self.okbtn.pack(side = "top")
    self.yearentry = Entry()
    self.yearentry.pack(side = "top")
    self.yearcontents = StringVar()
    self.yearcontents.set("2000")
    self.yearentry["textvariable"] = self.yearcontents
    self.yearentry.bind('<Key-Return>', self.judge())
  

  def judge(self):
    yearstr = self.yearcontents.get()
    year = int(yearstr)
    if year % 400 == 0:
      self.yearcontents.set(yearstr + "是闰年")
    elif year % 100 == 0:
      self.yearcontents.set(yearstr + "不是闰年")
    elif year % 4 == 0:
      self.yearcontents.set(yearstr + "是闰年")
    else:
      self.yearcontents.set(yearstr + "不是闰年")


root = Tk()
app = LeafYear(master = root)
root.title("闰年判断")
root.geometry("640x480")
app.mainloop()
