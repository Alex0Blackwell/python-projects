# Recursively test if a string is a palindrome


def palindrome(st):
    orig = st  # To check if forwards equals backwards
    reverse = ''
    pal = False
    if(len(st) == 1):  # Base case
        reverse = st[0]

    else:
        reverse = palindrome(st[1:])[0] + st[0]  # Recursive step

    if(reverse == orig):
        # Check if the original string is equal to the reverse
        pal = True
    return (reverse, pal)


string = input("Enter a palindrome")
print(palindrome(string))
