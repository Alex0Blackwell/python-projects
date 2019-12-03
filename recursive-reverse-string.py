# Recursively reverse a string


def reverse(st):
    # Tip and tail recursion to reverse a string
    if(len(st) == 1):  # Basis of recursion
        res = st[0]
    else:
        res = reverse(st[1:]) + st[0]  # Recursive step
    return res


string = "tshdfs23gdsg"
print(reverse(string))
