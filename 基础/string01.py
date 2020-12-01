str1 = "abcdefg"
print(str1[1])
print(type(str1[0]))

print(str1.find("a",0,7))
print(str1.index("d",0,7))
print(str1.count("d",0,7))

newstr = str1.replace("a","#")
print(str1)
print(newstr)


