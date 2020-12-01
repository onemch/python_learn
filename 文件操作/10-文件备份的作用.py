f = open('aaa.txt','r+')
back = f.read()
f.close()
f = open('aaa_back.txt','w+')
f.write(back)
f.close()

