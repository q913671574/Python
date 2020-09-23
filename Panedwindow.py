from tkinter import *

m1 = PanedWindow(showhandle=True, sashrelief=SUNKEN)
#showhandle显示手柄，默认位置为距离左端8像素，
#sashrelief=SUNKEN，设置分割线样式，默认为FLAT
#handlesize设置手柄大小，默认为8像素
#relief设置边框样式，默认为FLAT
m1.pack()


left = Label(m1, text="left pane")
m1.add(left)

m2 = PanedWindow(orient=VERTICAL, showhandle=True, sashrelief=SUNKEN)
#orient=VERTICAL 垂直分布，默认为水平分布(HORIZONTAL)
m1.add(m2)

top = Label(m2, text="top pane")
m2.add(top)

bottom=Label(m2, text="bottom pane")
m2.add(bottom)

right = Label(m1, text="rightpane")
m1.add(right)

mainloop()
