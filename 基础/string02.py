str1 = "abcdefg"

newstr = str1.replace("a","#")
print(str1)
print(newstr)

str2 = "a and b and c and d"
list2 = str2.split("and",2)
print(list2)

list3 = str2.split("and")
str3 = "=====".join(list3)
print(str3)