from tkinter import *


def callback():
    print("你好~")


root = Tk()

menubar = Menu(root)

openVar = IntVar()
saveVar = IntVar()
quitVar = IntVar()


filemenu = Menu(menubar, tearoff=False)
filemenu.add_checkbutton(label="打开", command=callback, variable=openVar)
filemenu.add_checkbutton(label="保存", command=callback, variable=saveVar)
filemenu.add_separator()
filemenu.add_checkbutton(label="退出(quit)", command=callback, variable=quitVar)
#为filemenu 菜单添加选项
menubar.add_cascade(label="文件", menu=filemenu)
#将filemenu菜单添加进menubar(主菜单)中

editVar = IntVar()

editmenu = Menu(menubar,tearoff=False)
editmenu.add_radiobutton(label="剪切", command=callback, variable=editVar, value=1)
editmenu.add_radiobutton(label="复制", command=callback, variable=editVar, value=2)
editmenu.add_radiobutton(label="粘贴", command=callback, variable=editVar, value=3)
menubar.add_cascade(label="编辑", menu=editmenu)
#将editmenu添加进filemenu中



editmenu2 = Menu(menubar, tearoff=True)
editmenu2.add_command(label="剪切2", command=callback)
editmenu2.add_command(label="复制2", command=callback)
editmenu2.add_command(label="粘贴2", command=callback)
filemenu.add_cascade(label="编辑2", menu=editmenu2)


root.config(menu=menubar)

mainloop()
