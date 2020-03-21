class Square:
    def __init__(self,l,w):
        self.width = w
        self.length = l
    def area(self):
        return self.width*self.length
squre = Square(10,20)
print(squre.area())