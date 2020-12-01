import functools

list1 = [1,2,3,4,5,6,7,8,9,10]

def sum(a,b):
    return a + b

res = functools.reduce(sum,list1)
print(res)