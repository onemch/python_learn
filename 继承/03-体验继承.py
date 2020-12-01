class Father():
    def __init__(self):
        self.num = 123

    def printInfo(self):
        print(self.num)

class Child(Father):
    pass

res = Child()
res.printInfo()