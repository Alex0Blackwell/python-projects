# Check if prime


def isPrime(num):
    # Runs in O(n)
    prime = True, "nothing muliplies"
    for a in range(2, num):
        if(num % a == 0):  # If there is a smaller number that multiplies
            prime = False, f"{int(num/a)} * {a}"
            break
    return prime


number = int(input("Check if a number is prime:\n"))
print(isPrime(number))
