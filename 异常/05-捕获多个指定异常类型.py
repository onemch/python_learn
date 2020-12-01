try:
    print(1/0)
except (ZeroDivisionError,NameError):
    print('error')