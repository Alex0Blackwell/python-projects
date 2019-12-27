# Average children in family calculator
# Made for a curious friend


def getAvg(lst):
    # Sum up all the elements in a list and then divide by how many are in the list
    res = 0
    for el in lst:
        res += el
    res /= len(lst)
    return round(res, 2)


def main():
    childLst = []  # List with the number of how many children in a family
    usrIn = ''
    c = 0
    while(usrIn != 'e'):  # Type 'e' to end
        usrIn = input(f"how many people are in family {c+1}? (e to end):\n")
        if(usrIn.isdigit()):
            childLst += [int(usrIn)]
        c += 1  # To keep track of how many families have been entered
    print("calculating...\nThe average children per family is:")
    print(getAvg(childLst))  # Display average number of children


main()
