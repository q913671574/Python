from tkinter import *
import webbrowser

root = Tk()

text = Text(root, width=30, height=5)
text.pack()

text.insert(INSERT, "I love FishC.com")

text.tag_add("link", "1.7", "1.16")
#设置一个tag名为link， 范围是1.7到1.16(第8个字符到第17个字符)
text.tag_config("link", foreground="blue", underline=True)
#设置link的属性，foreground 前景色(字体颜色);background 背景色; underline 有无下划线

def show_arrow_cursor(event):
    text.config(cursor="arrow")
#将text的cursor参数设置为arrow

def show_xterm_cursor(event):
    text.config(cursor="xterm")
#将text的cursor参数设置为xterm

def click(event):
    webbrowser.open("http//www.fishc.com")
#打开指定网页

text.tag_bind("link", "<Enter>", show_arrow_cursor)
#鼠标进入link的范围时调用show_arrow_cursor
text.tag_bind("link", "<Leave>", show_xterm_cursor)
#鼠标离开link的范围时调用show_xterm_cursor
text.tag_bind("link", "<Button-1>", click)
#鼠标点击时调用click

mainloop()
