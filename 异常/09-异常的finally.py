try:
    print(1/0)
except Exception as result:
    print(result)
else:
    print('ok')
finally:
    print('go away')