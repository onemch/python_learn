a = 100

def aa():
    print(a)

def bb():
    global a
    a = 200
    print(a)

print(a)
aa()
bb()
print(a)