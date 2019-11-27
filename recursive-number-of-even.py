def sumr(lst):
    res = 0
    if(len(lst) == 1):
        if(lst[0] % 2 == 0):
            res = 1
    else:
        if(lst[0] % 2 == 0):
            res = 1 + sumr(lst[1:])
        else:
            res = 0 + sumr(lst[1:])
    return res


lst = [1, 3, 2, 1, 6, 4]
print(sumr(lst))
