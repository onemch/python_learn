dict0 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# keys
print("#keys####################")
for key in dict0.keys():
    print(key)

# values
print("#values####################")
for v in dict0.values():
    print(v)

# items
print("#items####################")
for item in dict0.items():
    print(item)

# items拆包
print("#items拆包####################")
for key, value in dict0.items():
    print(f"{key}={value}")


# for a in dict0:
#     print(a)
