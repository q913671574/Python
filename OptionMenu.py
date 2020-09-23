from tkinter import *

OPTIONS = [
    "California",
    "458",
    "FF",
    "ENZO",
    "Laferrari"
    ]

root = Tk()

variable = StringVar()
variable.set(OPTIONS[0])

w = OptionMenu(root, variable, *OPTIONS)
#*在实参前表示解包，把OPTIONS列表分解为单个对象(否则作为一个整体选项)
#*作为形参表示打包
w.pack()


mainloop()

