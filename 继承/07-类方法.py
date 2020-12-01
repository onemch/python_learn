class Dog():
    __name = 'jack'

    @classmethod
    def get_name(cls):
        return cls.__name

print(Dog.get_name())

d1 = Dog()



print(d1.get_name())