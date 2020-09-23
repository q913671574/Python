from tkinter import *


def callback(event):
    print("点击位置", event.x, event.y)
#打印鼠标点击的位置

def callback2(event):
    print(event.keysym)
#打印按下的按键名，event.char打印按下的按键字符(功能键ALT等空显示) keycode 按键码

def callback3(event):
    print("当前位置", event.x, event.y)
#打印鼠标当前位置

root = Tk()

frame = Frame(root, width=200, height=200)
frame.bind("<Button-1>", callback)
frame.bind("<Key>", callback2)
frame.bind("<Motion>", callback3)
#<> 称为时间序列， ButtonRelese 释放鼠标才有效，Button按下鼠标就有效
frame.focus_set()

frame.pack()


mainloop()
