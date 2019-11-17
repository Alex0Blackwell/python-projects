def checkRegular(usrVerb):
    pass  # later


def clean(origVerb):
    cleanVerb = origVerb
    placement = 0
    for char in origVerb:
        if(char == 'é' or char == 'ê'):
            origVerb[placement] = 'e'
        if(char == 'ï' or char == 'î'):
            origVerb[placement] = 'i'
        placement += 1
    return cleanVerb


def main():
    usrVerb = input("Enter the French verb you wish to conjugate:\n")
    usrPronoun = input("Enter the pronoun you wish to conjugate for:\n")
    cleanVerb = clean(usrVerb)
    checkRegular()



main()
