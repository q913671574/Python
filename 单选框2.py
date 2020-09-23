from tkinter import *

root =Tk()



group = LabelFrame(root, text="最好的脚本语言是？", padx=5, pady=5)
group.pack(padx=10, pady=10)

LANGS = [
    ("Python", 1),
    ("Perl", 2),
    ("Ruby", 3),
    ("Lus", 4)]

v = IntVar()

for lang, num in LANGS:
    b = Radiobutton(group, variable=v, value=num, text=lang)
    #indicatoron=False 将单选框设置为按钮形式
    b.pack(fill=X)
    #fill=X 将单选框填充改为x方向填充
