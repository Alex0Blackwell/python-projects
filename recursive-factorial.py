# Three different methods to compute a factorial
# One with recursion,
# one with a for loop,
# and one with a while loop


def factorialRecursion(n):
    # Recursive factorial
    if(n == 1):  # Basis
        return 1
    else:
        return n * factorialRecursion(n-1)  # Recursive step


def factorialFor(n):
    # Factorial with for loop
    res = 1
    for i in range(1, n+1):  # Iterative step
        res = res * i
    return res


def factorialWhile(n):
    # Factorial with while loop
    res = 1
    while(n > 0):  # Iterative step
        res *= n
        n -= 1
    return res


# Print the factorial of the given number
number = 5
print(f"Factorial of {number}")
print(factorialRecursion(number))
print(factorialFor(number))
print(factorialWhile(number))
