from tkinter import *


def callback():
    print("你好~")


root = Tk()

menubar = Menu(root)


filemenu = Menu(menubar, tearoff=False)
filemenu.add_command(label="打开", command=callback)
filemenu.add_command(label="保存", command=callback)
filemenu.add_separator()
filemenu.add_command(label="退出(quit)", command=callback)
#为filemenu 菜单添加选项
menubar.add_cascade(label="文件", menu=filemenu)
#将filemenu菜单添加进menubar(主菜单)中

editmenu = Menu(menubar,tearoff=False)
editmenu.add_command(label="剪切", command=callback)
editmenu.add_command(label="复制", command=callback)
editmenu.add_command(label="粘贴", command=callback)
filemenu.add_cascade(label="编辑", menu=editmenu)
#将editmenu添加进filemenu中


editmenu2 = Menu(menubar, tearoff=True)
editmenu2.add_command(label="剪切2", command=callback)
editmenu2.add_command(label="复制2", command=callback)
editmenu2.add_command(label="粘贴2", command=callback)
menubar.add_cascade(label="编辑2", menu=editmenu)


root.config(menu=menubar)

mainloop()
