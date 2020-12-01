#create
s1 = {1,2,3,4}
print(s1)
s2 = set("abcdefg")
print(s2)
s3 = {1,1,1,2,2,2,3,4,4}
print(s3)

s4 = {}
print(type(s4))
s5=set()
print(type(s5))

#add
s1 = {1,2,3,4}
s1.add("asdf")
print(s1)

#update
s1 = {1,2,3,4}
s1.update([1,11,23,43])
print(s1)

#remove
s1 = {1,2,3,4}
s1.remove(2)
print(s1)

#discard
s1 = {1,2,3,4}
s1.discard(7)
print(s1)

#pop
s1 = {1,2,3,4}
delnum = s1.pop()
print(delnum)
print(s1)

#是否存在
s1 = {1,2,3,4}
print(1 in s1)
print(123 in s1)