list1 = [1,2,3,4,5,6,7,8,9,10]

def getNum(x):
    return x %2

res = filter(getNum,list1)
print(res)

print(list(res))