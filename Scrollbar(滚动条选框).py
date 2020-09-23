from tkinter import *

root = Tk()

sb = Scrollbar(root)
sb.pack(side=RIGHT, fill=Y)
#左对齐，y方向填充
lb = Listbox(root, yscrollcommand=sb.set)

for i in range(1000):
    lb.insert(END, i)

lb.pack(side=LEFT, fill=BOTH)

sb.config(command=lb.yview)

mainloop()
