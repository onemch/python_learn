class Dog():
    color = 'black'

d1 = Dog()
d2 = Dog()

print(Dog.color)
print(d1.color)

d1.color = '123'
print(d1.color)
print(Dog.color)
Dog.color = '789'
print(Dog.color)
print(d2.color)