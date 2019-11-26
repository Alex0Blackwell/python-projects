def factorialRecursion(n):
    if(n == 1):
        return 1
    else:
        return n * factorialRecursion(n-1)


def factorialFor(n):
    res = 1
    for i in range(1, n+1):
        res = res * i
    return res


def factorialWhile(n):
    res = 1
    while(n > 0):
        res *= n
        n -= 1
    return res


number = 5
print(f"Factorial of {number}")
print(factorialRecursion(number))
print(factorialFor(number))
print(factorialWhile(number))
