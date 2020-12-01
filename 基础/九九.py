
j=1
while j<10:
    i = 1
    while i <= j:
        print(str(j)+'*'+str(i)+'='+str(j*i), end="  ")
        i = i + 1
    j+=1;
    print()