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
    pass

res = Child()
print(res.num)
res.printInfo()

print(Child.__mro__)