filename = input('input filename :')
dotIndex = filename.rfind('.')
newFileName = filename[:dotIndex] + '_bak_' + filename[dotIndex:]

old_f = open(filename,'rb')
new_f = open(newFileName,'wb')

while True:
    tmp = old_f.read(1024)
    if len(tmp) == 0:
        break
    new_f.write(tmp)

old_f.close()
new_f.close()