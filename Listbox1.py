from tkinter import *


master = Tk()

theLB = Listbox(master, selectmode=BROWSE， height=11)
#创建一个Listbox 对象，selectmode 选择模式，SINGLE 为单选，只能点击来选；BROWSE(默认参数) 单选，可以拖动鼠标来选择。还有两个多选模式：
#height=11设定显示的项目数(默认为10，当选项大于10时，可通过鼠标的滚轮查看选项)
theLB.pack()

for item in ["鸡蛋", "鹅蛋", "鸭蛋", "李狗蛋"]:
    theLB.insert(END, item)
    #每次在末尾添加选项

theButton = Button(master, text="删除此选项",\
                   command=lambda x=theLB:x.delete(ACTIVE))

#Listbox.delete() 可传入1-2个参数，传入两个参数删除指定范围选项；传入一个参数，只删除指定位置选项


theButton.pack()

mainloop()
