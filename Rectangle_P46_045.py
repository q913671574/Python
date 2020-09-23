class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    def __setattr__(self, name, value):
        if name == 'square':
            self.width = value
            self.height = value
        else:
            super().__setattr__(name, value) #若直接写self.name = value,将会一直调用__setattr__方法
    def getArea(self):
        return self.width * self.height

        
