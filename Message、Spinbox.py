from tkinter import  *

root = Tk()

w1 = Message(root, text="这是一\n则消息", width=100)
w1.pack()

w2 = Message(root, text="这是\n一则骇人听闻的长长长长长长长长消息！", width=100)
w2.pack()

w = Spinbox(root, values=("小甲鱼", "风介", "wei_Y", "戴宇轩"), wrap=True)
#wrap = True 循环滚动
w.pack()

mainloop()
