list1 = ["Tom","Jack","lily"]
print(list1)
print(len(list1))
print(list1.index("Tom",0,2))
print(list1.count("Tom"))

#append
list1 = ["Tom","Jack","lily"]
list1.append("Mac")
list1.append(["Mac","Sun"])
print(list1)

#entend
list1 = ["Tom","Jack","lily"]
list1.extend(["Mac","Sun"])
print(list1)
list1.extend("micro")
print(list1)

#insert
list1 = ["Tom","Jack","lily"]
list1.insert(1,"aoy")
print(list1)

#del
list1 = ["Tom","Jack","lily"]
#del list1
#del(list1)
del list1[0]
print(list1)

#pop
#list1.pop(1)
list1 = ["Tom","Jack","lily"]
name =  list1.pop()
print(name)
print(list1)

#remove
list1 = ["Tom","Jack","lily"]
list1.remove("Jack")
print(list1)

#clear
list1 = ["Tom","Jack","lily"]
list1.clear()
print(list1)


#edit
list1 = ["Tom","Jack","lily"]
list1[1] = "aaa"
print(list1)

#reverse
list1 = [5,2,9,3,1,6]
list1.reverse()
print(list1)

#sort
list1 = [5,2,9,3,1,6]
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)

#copy
list1 = ["Tom","Jack","lily"]
list2 = list1.copy()
print(list2)