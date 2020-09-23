from tkinter import *
import hashlib


def check():
    contents = text.get("1.0", END)
    if sig != getSig(contents):
        print("警告：内容发生变动！")
    else:
        print("风平浪静~")

def getSig(contents):
    m = hashlib.md5(contents.encode())
    return m.digest()

        
root = Tk()

text = Text(root, width=30, height=5)
text.pack()

text.insert(INSERT, "I love FishC.com!")
contents = text.get("1.0", END)


sig = getSig(contents)


Button(root, text="检查", command=check).pack()

mainloop()
