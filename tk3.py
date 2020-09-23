from tkinter import *

root = Tk()

textLabel = Label(root, text="FBI Warning!", justify=LEEF)
#创建一个Label,传入文本"FBI Warning", justify 对齐方式，默认为居中(center)
textLabel.pack(side=LEFT)

photo = PhotoImage(file = "")
#指定图片路径file,并用photo标签
imgLabel = Label(root, imge = photo)
#创建一个Label，传入图片photo
imgLabel.pack(side=RIGHT)


mainloop()
#左边一行文字，右边一个图片
