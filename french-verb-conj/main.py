# def checkRegular(usrVerb):
#     if(usrVerb in)


def clean(origVerbs):
    cleanVerbs = []
    for i in range(len(origVerbs)):
        verb = origVerbs[i]
        cleanVerb = verb.replace("é" or "ê", "e")
        cleanVerb = cleanVerb.replace(" ", "")
        irregFile = open("irregularVerbs.txt", "a")
        irregFile.write(f"{cleanVerb}\n")
        irregFile.close()
        cleanVerbs += [cleanVerb]
        # placement = 0
        # currentVerb = origVerbs[i]
        # for char in origVerbs[i]:
        #     if(char == 'é' or char == 'ê'):
        #         currentVerb[placement] = 'e'
        #     if(char == 'ï' or char == 'î'):
        #         currentVerb[placement] = 'i'
        #     if(char == ' '):
        #         currentVerb[placement] = ''
        #     placement += 1
        # cleanVerbs += [currentVerb]
    return cleanVerbs


def main():
    irregFile = open("irregularVerbs.txt", "r")
    irregVerbs = irregFile.read().splitlines()
    irregFile.close()

    cleanIrregs = clean(irregVerbs)

    print(cleanIrregs)

    # usrVerb = input("Enter the French verb you wish to conjugate:\n")
    # usrPronoun = input("Enter the pronoun you wish to conjugate for:\n")
    # cleanVerb = clean(usrVerb)
    # print(f"You imputted")
    # checkRegular(usrVerb)


main()
