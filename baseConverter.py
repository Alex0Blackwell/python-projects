# Base conversion algorithm
# Fastest way to convert bases
# Note this does it in reverse so the strings and the strings elements
# must be reversed


def baseConvert(num, base):
    # Given a number and a base to convert to
    res = ''
    q = num
    while(q > 0):
        r = q % base
        # Reverse string because the whole string will eventually be reversed
        res += ',' + str(r)[::-1]
        q = q // base
    return res[::-1]  # Return the whole string reversed


usrNum = int(input("Enter a number to convert:\n"))
usrBase = int(input("Enter a base:\n"))
print(baseConvert(usrNum, usrBase))
