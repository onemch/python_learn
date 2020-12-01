def testPrint(str,a=1):
    print(str)
    return None

def testPrint1(str,*a):
    print(str)
    for i in a:
        print(i)
    return None

testPrint("aaa")
testPrint1("",1,2,3,4)