import  os

flag = 2

dirlist = os.listdir()

for i in dirlist:
    if flag == 1:
        newName = 'py_' + i
        os.rename(i,newName)
    elif flag == 2:
        preStr = len('_py')
        newName = i[preStr:]
        os.rename(i,newName)