def fibonacci(length):
    res = [1, 1]
    for i in range(2, length):
        res += [res[i-2] + res[i-1]]
    return res


print(fibonacci(10))
