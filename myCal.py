# -*- coding:UTF-8  -*-

from tkinter import *


class MyCal(Tk):

  def initGUI(self):
    self.title = '计算器'
    self.geometry('640x480')
    l1 = Label(self, text='操作数1:', bg='pink')
    l1.pack()
    self.mainloop()

mc = MyCal()
mc.initGUI() 
