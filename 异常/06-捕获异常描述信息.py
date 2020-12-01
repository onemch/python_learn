try:
    print(1/0)
except (ZeroDivisionError,NameError) as result:
    print(result)