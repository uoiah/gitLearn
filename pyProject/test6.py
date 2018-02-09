# -*- coding:UTF-8 -*-

from tkinter import *

class LoginFrame(Frame):
  def __init__(self, master=None):
    super().__init__(master)
    l1 = Label(self, text='用户名：').grid(row=0, column=0, padx=10, pady=2, sticky='e')
    tvalue = StringVar()
    tvalue.set('tom')
    t1 = Entry(self, textvariable=tvalue).grid(row=0, column=1, padx=10, pady=2, sticky='e')
    l2 = Label(self, text='密  码：').grid(row=1, column=0, padx=10, pady=2, sticky='e') 
    tvalue1 = StringVar()
    tvalue1.set('')
    t2 = Entry(self, textvariable=tvalue1, show='*').grid(row=1, column=1, padx=10, pady=2, sticky='e')
    b1 = Button(self, text='登录').grid(row=2, column=0, padx=10, pady=2,sticky='e')
    b2 = Button(self, text='重置').grid(row=2, column=1, padx=10, pady=2,sticky='e')
    self.pack() 


root = Tk()
root.title('登录')
root.geometry('640x480')
loginf = LoginFrame(root)
loginf.mainloop()

