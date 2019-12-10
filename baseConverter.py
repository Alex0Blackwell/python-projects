# Base conversion algorithm


def baseConvert(num, base):
    res = ''
    q = num
    while(q > 0):
        r = q % base
        res += ',' + str(r)[::-1]
        q = q // base
    return res[::-1]


usrNum = int(input("Enter a number to convert:\n"))
usrBase = int(input("Enter a base:\n"))
print(baseConvert(usrNum, usrBase))
