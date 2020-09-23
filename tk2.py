import tkinter as tk

    
class APP:
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack(side=tk.BOTTOM, padx=10, pady=10)
        #padx 到左边框的距离, pady 到上边框的距离;side 位置，可选：LEFT, RIGHT, TOP, BOTTOM 

        self.hi_there = tk.Button(frame, text="打招呼", fg="blue", command=self.say_hi, bg="green")
        #text 所显示的文本; fg 字体颜色; bg 按钮背景颜色; command 按钮被按下之后的动作(代码)
        self.hi_there.pack()

    def say_hi(self):
        print("你按了一下按钮-_-#")

root = tk.Tk()
app = APP(root)

root.mainloop()
