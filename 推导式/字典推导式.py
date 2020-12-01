dict1 = {i:i**2 for i in range(1,5)}
print(dict1)

list1 = ["name","age","gender"]
list2 = ["haha","12","男"]
dict2 = {list1[i]: list2[i] for i in range(len(list1))}
print(dict2)

dict3 = {"a" : 12 , "b" : 5 , "c" : 9 , "d" : 13}
count = {k : v for k,v in dict3.items() if v >10}
print(count)