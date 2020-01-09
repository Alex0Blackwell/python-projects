# Add two binary numbers


def addNums(num1, num2):
    # Add the two binary numbers together using logic to get another
    # binary number
    res = ""
    carry = 0
    i = 0
    while(i < len(min(num1, num2, key=len)) or carry == 1):
        if(not(i < len(min(num1, num2, key=len)))):
            # Then we must carry the final 1
            res = '1' + res
            carry = 0
        else:
            num1Dig = int(num1[-(i+1)])
            num2Dig = int(num2[-(i+1)])

            if(num1Dig == 0):
                if(num2Dig == 0):
                    if(carry == 1):
                        res = '1' + res
                    else:
                        res = '0' + res
                    carry = 0
                else:
                    if(carry == 1):
                        res = '0' + res
                        carry = 1
                    else:
                        res = '1' + res
                        carry = 0
            else:
                if(num2Dig == 0):
                    if(carry == 1):
                        res = '0' + res
                        carry = 1
                    else:
                        res = '1' + res
                        carry = 0
                elif(num2Dig == 1 and carry == 1):
                    res = '1' + res
                    carry = 1
                else:
                    res = '0' + res
                    carry = 1
        i += 1
    return res


def main():
    num1 = input("Enter the first number in binary:\n")
    num2 = input("Enter the second number in binary: \n")

    addedNumber = addNums(num1, num2)
    print(f"The binary numbers \n\"{num1}\"\nand \n\"{num2}\"\nadded together is \"{addedNumber}\"")


main()
