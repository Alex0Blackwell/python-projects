# FizzBuzz coding interview question


def fizzBuzz(num):
    res = ''
    if(num % 3 == 0):
        res += 'Fizz '
    if(num % 5 == 0):
        res += 'Buzz'
    return res


usrNum = ''
while(not usrNum.isdigit()):
    usrNum = input('Enter a number: ')
usrNum = int(usrNum)
print(fizzBuzz(usrNum))
