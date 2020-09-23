from tkinter import *

def callback():
    var.set("吹吧你，我才不信呢~")


root = Tk()


frame1 = Frame(root)
frame2 = Frame(root)


var = StringVar()
var.set("满18周岁才能观看\n你是否已满18岁？")#设置一个可变的文本
textLabel = Label(frame1,
                  textvariable=var,
                  justify=LEFT)
#justify 文本对齐方式默认是CENTER
textLabel.pack(side=LEFT)

photo = PhotoImage(file = "")
#指定图片路径file,并用photo标签
imgLabel = Label(root, image = photo)
#创建一个Label，传入图片photo
imgLabel.pack(side=RIGHT)

theButton = Button(frame2, text="我已满18周岁", command=callback)
theButton.pack()

frame1.pack(padx=10, pady=10)
frame2.pack(padx=10, pady=10)


mainloop()
#左边一行文字，右边一个图片
