from tkinter import *
import hashlib

root = Tk()

text = Text(root, width=30, height=5)
text.pack()

text.insert(INSERT, "I love FishC.com!o")

def getIndex(text, index):
    return tuple(map(int, str.split(text.index(index), ".")))

#text.index()返回1.3；str.split(text.index(index), "." ，分割字符串 返回['1', '3']；
#map(int, str.split(text.index(index), ".")) 对分割出来的的字符串进行强制转化int()，返回<map object at 0x0000000003254308> 
#tuple(map())强制转化为元组 返回(1, 3)

start = "1.0"
#搜索起始点。 第一行第一列(1.0)

while True:
    pos = text.search("o", start, stopindex=END)
    if not pos:
        break
    print("找到啦，位置是：", getIndex(text, pos))
    start =pos + "+1c"


mainloop()
