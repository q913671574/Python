from tkinter import *

root = Tk()

photo = PhitiImage(file="")
theLabel = Label(root,
                 text="学Python\n到 FishC.",
                 justify=LEFT,
                 image=photo,
                 compound=CEMTER,
                 font=("宋体", 20),
                 fg="white")
#font 选择字体、字号; compound 图片的显示位置(bottom/top/left/right/center/None(默认)) 设为center则表示文本在图片上面
theLabel.pack()


imgLabel.pack(side=RIGHT)
