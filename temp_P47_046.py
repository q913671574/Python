class Celsius:
    def __init__(self, value = 26.0):
        print('c的init')
        self.value = float(value)

    def __get__(self, instance, owner):
        print('c的get')
        return self.value

    def __set__(self, instance, value):
        print('c的set')
        self.value = float(value)

class Fahrenheit:
    def __get__(self, instance, owner):
        print('f的get')
        return instance.cel * 1.8 + 32

    def __set__(self, instance, value):
        print('f的set')
        instance.cel = (float(value) -32) / 18
#self 表示Celsius 或Fahrenheit 实例出来的Temperature的属性即cel、fah。用self代表Temperature的属性 cel、fah
#instance 表示Temperature实例化的对象temp
#调用instance.cel  就是调用temp.cel。用instance代表实例化的对象


class Temperature:
    cel = Celsius()
    fah = Fahrenheit()


temp = Temperature()
