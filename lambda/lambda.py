f1 = lambda : 100
print(f1())

f2 = lambda a : a
print(f2('hello aaaa!!!'))

f3 = lambda a,b,c=100:a+b+c
print(f3(1,2))

f4 = lambda *args : args
print(f4(1,2,3))

f5 = lambda **kwargs : kwargs
print(f5(name=999,age=000))

f6= lambda a,b : a if a>b else b
print(f6(9,7))