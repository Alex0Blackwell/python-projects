# Average children in family calculator


def getAvg(lst):
    res = 0
    for el in lst:
        res += el
    res /= len(lst)
    return round(res, 2)


def main():
    childLst = []
    usrIn = ''
    c = 0
    while(usrIn != 'e'):
        usrIn = input(f"how many people are in family {c+1}? (e to end):\n")
        if(usrIn.isdigit()):
            childLst += [int(usrIn)]
        c += 1
    print("calculating\nThe average children per family is:")
    print(getAvg(childLst))


main()
