def fun():
    try:
        print('1')
        db = 'SessionLocal()'
        yield db
    finally:
        print('3')


# for i in fun():
#     print(i)
#     print('2')


# print(next(fun()))
j = 100
for i in fun():
    j += 1
    print(j)
