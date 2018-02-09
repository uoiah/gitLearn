# -*- coding: UTF-8 -*-

from tkinter import *


root = Tk()
root.title('简易计算器')
root.geometry('640x480')
root.resizable(width = True, height = False)
ll = Label(root, text = 'label', bg = 'red', font=('Arail', 12), width = 8, height = 3).pack()
f1 = Frame(root)
f_left = Frame(f1)
l1 = Label(f_left, text = 'label', bg = 'pink', font=('Arail', 12)).pack(side = TOP)
var = Variable()
t1 = Entry(f_left, textvariable = var)
var.set('5')
t1.pack()
f_left.pack(side = LEFT)
f_right = Frame(f1)
l3 = Label(f_right, text = 'label', bg = 'pink', font=('Arail', 12))
l3.pack(side = RIGHT)
l4 = Label(f_right, text = 'label', bg = 'pink', font=('Arail', 12))
l4.pack(side = RIGHT)
f_right.pack(side = RIGHT)
f1.pack()
root.mainloop()
