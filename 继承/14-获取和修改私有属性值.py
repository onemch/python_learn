class Father():
    def __init__(self):
        self.__money = 5000
    def get_money(self):
        return  self.__money

class Child(Father):
    pass

res = Child()
print(res.get_money())