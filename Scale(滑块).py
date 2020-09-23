from tkinter import *

root = Tk()

s1 = Scale(root, from_=0, to=42, tickinterval=20, resolution=5, length=200)
s1.pack()

s2 = Scale(root, from_=0, to=200, orient=HORIZONTAL, tickinterval=10, length=600)
#orient=HORIZONTAL 水平放置; tickinterval=10, 刻度间隔10; resolution=5， 滑块最小滑动间隔;length滑动条长度(单位：像素)
s2.pack(padx=100)

def show():
    print(s1.get(), s2.get())

Button(root, text="获取位置", command=show).pack()



mainloop()
