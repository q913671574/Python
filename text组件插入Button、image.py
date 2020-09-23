from tkinter import *

root = Tk()

text = Text(root, width=30, height=30)
text.insert(INSERT, "点击按钮插入图片")
text.pack()

photo = PhotoImage(file="")

def show():
    text.image_create(END, image=photo)
    print("图片已插入")

b1 = Button(text, text="点我点我", command=show)
text.window_create(INSERT, window=b1)

mainloop()
