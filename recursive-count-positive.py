# Recursively count the number of even integers in a list


def countEven(lst):
    res = 0
    if(len(lst) == 1):
        if(int(lst[0]) % 2 == 0):
            res = 1
    else:
        if(int(lst[0]) % 2 == 0):
            res = 1 + countEven(lst[1:])
        elif(int(lst[0]) % 2 != 0):
            res = 0 + countEven(lst[1:])
    return res


lst1 = [4, '3', 6, 2, 67, '2', 2]
numPositive = countEven(lst1)
print(numPositive)
