f = open('tet.txt','a+')

f.seek(1,0)

print(f.read())

f.close()