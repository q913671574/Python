from tkinter import *

root = Tk()
root.title("Root")

def create():
    top = Toplevel()
    top.title("FishC Demo")

    msg = Message(top, text="I love FishC.com")
    msg.pack()

top1 = Toplevel()
#Toplevel 只能依附于 Tk(),不能单独使用
top1.title("主窗口")

Button(top1, text="创建顶级窗口", command=create).pack()

mainloop()
