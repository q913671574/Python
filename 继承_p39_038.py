class Turtle:
    def __init__(self, x):
        self.num = x

class Fish:
    def __init__(self, x):
        self.num = x

class Pool:
    def __init__(self, x, y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)
        #组合，将几个类放在一起
    def print_num(self):
        print('乌龟有%d个，鱼有%d个。' % (self.turtle.num, self.fish.num))

pool = Pool(1, 10)
pool.print_num()









"""class Fish():
    speed = 5
    hunger = 10
    def eat(self):
        self.hunger -= 1
        print('当前饥饿值为: %d ' % self.hunger)
    def tire(self):
        self.speed -= 1
        print('当前速度为: %d' % self.speed)
    def Myspeed(self):
        print('当前速度为: %d' % self.speed)
    def Myhunger(self):
        print('当前饥饿值为: %d ' % self.hunger)
        
class San(Fish):
    speed = 6
    hunger = 8
    
class Sha(Fish):
    speed = 4
    hunger = 7

yu1 = San()
yu2 = Sha()
yu1.Myspeed()
yu1.Myhunger()
print('下面是yu2')
yu2.Myspeed()
yu2.Myhunger()
print('开始检验方法')
yu1.eat()
yu1.tire()
print('小鱼2')
yu2.eat()
yu2.tire()
"""



