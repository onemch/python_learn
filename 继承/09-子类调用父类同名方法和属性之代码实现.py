class Father1():
    def __init__(self):
        self.num = 111

    def printInfo(self):
        print(str(self.num) + '===========')


class Father2():
    def __init__(self):
        self.num = 222

    def printInfo(self):
        print(str(self.num) + '===========')

class Child(Father2,Father1,):
    def __init__(self):
        self.num = 33

    def printInfo(self):
        self.__init__()
        print(str(self.num) + '===========')

    def f1Print(self):
        Father1.__init__(self)
        Father1.printInfo(self)

res = Child()
print(res.num)
res.printInfo()

print(Child.__mro__)

res.f1Print()
res.printInfo()