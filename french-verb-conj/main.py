def checkIrregular(verb, allVerbs):
    res = False
    if(verb in allVerbs):
        res = True
    return res


def checkVerbEnd(verb):
    (ir, re, er) = False, False, False
    end = verb[-2:]
    if(end == 'ir'):
        ir = True
    elif(end == 're'):
        re = True
    elif(end == 'er'):
        er = True
    return (ir, re, er)


def regularConj(pro, verb, end):
    (ir, re, er) = end
    if(ir):
        print('verb is ir')
    elif(re):
        print('verb is re')
    elif(er):
        print('verb is er')


def main():
    irregFile = open("irregularVerbs.txt", "r")
    irregVerbs = irregFile.read().splitlines()
    irregFile.close()

    usrVerb = input("Enter the French verb you wish to conjugate:\n")
    usrPronoun = input("Enter the pronoun you wish to conjugate for:\n")

    isIrregular = checkIrregular(usrVerb, irregVerbs)
    endType = checkVerbEnd(usrVerb)
    print(isIrregular, endType)
    regularConj(usrPronoun, usrVerb, endType)



main()
