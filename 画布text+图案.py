from tkinter import *

root = Tk()

w = Canvas(root, width=200, height=100)
w.pack()

w.create_line(0, 0, 200, 100, fill="green", width=3)
w.create_line(200, 0, 0, 100, fill="green", width=3)
w.create_rectangle(40, 20, 160, 80, fill="green")
w.create_oval(40, 20, 160, 80, fill="pink")
#将椭圆/圆，放入矩形/正方形中来画
w.create_rectangle(65, 35, 135, 65, fill="white")
#创建2个嵌套矩形，小矩形可以为文字提供背景色


w.create_text(100, 50, text="FishC")
#100, 50  文本的中心位置(默认居中对齐方式)


mainloop()
