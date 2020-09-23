import time as t

class MyTimer():
    def __init__(self):
        self.unit = ['年', '月', '天', '小时', '分钟', '秒']
        self.prompt = '未开始计时！'
        self.lasted = []
        self.begin = 0
        self.end = 0

    
    def __str__(self):
        #打印出当前的状态
        return self.prompt 

    __repr__ = __str__
    
    

    #开始计时
    def start(self):
        if self.begin:
            print('正在计时！')
        else:
            self.begin = t.localtime()
            print('计时开始...')
            #定时器状态改变，随之改变prompt的内容
            self.prompt = '正在计时！'

    #停止计时
    def stop(self):
        if self.begin:
            self.end = t.localtime()
            print('计时结束!')
            self._calc()
            #计时完毕，将开始时间和结束时间置零
            self.begin = 0
            self.end = 0
        else:
            print('计时未开始！')

    #内部方法，计算运行时间
    def _calc(self):
        self.lasted = []
        self.prompt = '总共运行了'
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
        #将lasted中的负数更改为正确的正数
        if lasted[5]<0:
            lasted[5] = lasted[5] + 60
            lasted[4] = lasted[4] - 1
        if lasted[4]<0:
            lasted[4] = lasted[4] + 60
            lasted[3] = lasted[3] - 1
        if lasted[3]<0:
            lasted[3] = lasted[3] + 24
            lasted[2] = lasted[2] - 1
        if lasted[2]<0:
            lasted[2] = lasted[2] + 30
            lasted[1] = lasted[1] - 1
        if lasted[1]<0:
            lasted[1] = lasted[1] + 12
            lasted[0] = lasted[0] - 1

           
        print(self.prompt)




"""
import time as t

class MyTimer():
    def __init__(self):
        self.unit = ['年', '月', '天', '小时', '分钟', '秒']
        self.prompt = '未开始计时！'
        self.lasted = []
        self.begin = 0
        self.end = 0


    def __str__(self):
        return self.prompt 

    __repr__ = __str__
    
    

    #开始计时
    def start(self):
        if self.begin:
            print('正在计时！')
        else:
            self.begin = t.localtime()
            print('计时开始...')
            self.prompt = '正在计时！'

    #停止计时
    def stop(self):
        if self.begin:
            self.end = t.localtime()
            print('计时结束!')
            self._calc()
            self.begin = 0
            self.end = 0
            

        else:
            print('计时未开始！')

    #内部方法，计算运行时间
    def _calc(self):
        self.lasted = []
        self.prompt = '总共运行了'
        for index in range(6):
            if self.end[index]>=self.begin[index]:
                count = self.end[index] - self.begin[index]
            else:
                self.lasted[index-1] = self.lasted[index-1] - 1
                count = self.end[index] - self.begin[index] + 60 
            self.lasted.append(count)
        for index in range(6):
            if self.lasted[index]:
                self.prompt += str(self.lasted[index]) + self.unit[index]
        print(self.prompt)


"""
        
            
