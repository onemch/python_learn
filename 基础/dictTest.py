dict0 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print("dict['Name']: ",dict0['Name'])
print("dict['Name']: ", dict0['Name'])
print("dict['Age']: ", dict0['Age'])
# print(dict['123'])

#创建空字典
dict1 = {}
print(type(dict1))

dict3 = dict()
print(type(dict3))

dict0["id"] = 100
print(dict0)

#del
dict0 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# del dict0
# print(dict0)

del dict0["Name"]
print(dict0)

dict0.clear()
print(dict0)

#get
dict0 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("######get##########")
print(dict0.get("Name"))
print(dict0.get("Names"))
print(dict0.get("Names","Haha"))

#keys
dict0 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("######keys##########")
print(dict0.keys())

#values
dict0 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("######values##########")
print(dict0.values())

#items
dict0 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("######items##########")
print(dict0.items())