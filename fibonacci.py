# Program that, given the length of how many characters of the 
# fibonacci sequence is to be displayed, will display the fibonacci
# sequence.


def fibonacci(length):
    res = [1, 1]  # Base
    for i in range(2, length):
        res += [res[i-2] + res[i-1]]  # Recursive step
    return res


print(fibonacci(10))  # Length of 10
