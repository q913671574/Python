from tkinter import *


def show():
    print("账号：  %s" % e1.get())
    print("密码：  %s" % e2.get())

root = Tk()
root.title("LPH")

frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)

label1 = Label(frame1, text="账号：")
label2 = Label(frame2, text="密码：")

label1.pack(padx=5, pady=5, side=LEFT)
label2.pack(padx=5, pady=5, side=LEFT)

v1 = StringVar()
v2 = StringVar()


e1 = Entry(frame1, textvariable=v1)
e2 = Entry(frame2, textvariable=v2, show="*")
#show="*"  以*代替输入的字符

e1.pack(padx=5, pady=5)
e2.pack(padx=5, pady=5)



b1 = Button(frame3, text="登录", command=show, width=10, padx=5)
b2 = Button(frame3, text="退出", width=10, command=root.destroy, padx=5)
b1.pack(side=LEFT)
b2.pack(side=RIGHT)

frame1.pack(pady=10)
frame2.pack(pady=1)
frame3.pack(pady=1)



mainloop()
