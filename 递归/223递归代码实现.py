def num_sum(num):
    if num==1:
        return 1
    return num + num_sum(num-1)

res = num_sum(3)
print(res)