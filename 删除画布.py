from tkinter import *

root = Tk()

w = Canvas(root, width=200, height=100)
w.pack()

line1 = w.create_line(0, 50, 200, 50, fill="yellow")
#创建一条线，初始点为(0，50), 结束点为(200, 50)， 颜色为 yellow， 
line2 = w.create_line(100, 0, 100, 100, fill="red", dash=(4,4), width=3)
#dash=(4,4) 设置为虚线,width=3 设置宽度为3像素
rect1 = w.create_rectangle(50, 25, 150, 75, fill="blue")
#创建一个矩形，左上角位置(50, 25) 右下角位置(150, 75) ， 颜色为 blue

w.coords(line1, 0, 25, 200, 25)
#将line1的位置修改为(0, 25) (200, 25)  向上平移25
w.itemconfig(rect1, fill="red")
#将rect1的颜色设置为红色

Button(root, text="删除全部", command=(lambda x=ALL:w.delete(x))).pack()
#调用w的delete方法，删除ALL(画布上所有对象)


mainloop()
