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
    verbNoEnd = verb[:-2]

    if(pro == 'je'):
        if(ir):
            verbNoEnd += 'is'
        elif(re):
            verbNoEnd += 's'
        elif(er):
            verbNoEnd += 'e'
    elif(pro == 'tu'):
        if(ir):
            verbNoEnd += 'is'
        elif(re):
            verbNoEnd += 's'
        elif(er):
            verbNoEnd += 'es'
    elif(pro == 'il' or pro == 'elle' or pro == 'on'):
        if(ir):
            verbNoEnd += 'it'
        elif(re):
            pass
        elif(er):
            verbNoEnd += 'e'
    elif(pro == 'nous'):
        if(ir):
            verbNoEnd += 'issons'
        elif(re):
            verbNoEnd += 'ons'
        elif(er):
            verbNoEnd += 'ons'
    elif(pro == 'vous'):
        if(ir):
            verbNoEnd += 'issez'
        elif(re):
            verbNoEnd += 'ez'
        elif(er):
            verbNoEnd += 'ez'
    elif(pro == 'ils' or pro == 'elles'):
        if(ir):
            verbNoEnd += 'issent'
        elif(re):
            verbNoEnd += 'ent'
        elif(er):
            verbNoEnd += 'ent'

    return verbNoEnd


def main():
    irregFile = open("irregularVerbs.txt", "r")
    irregVerbs = irregFile.read().splitlines()
    irregFile.close()

    usrVerb = input("Enter the French verb you wish to conjugate:\n")
    usrPronoun = input("Enter the pronoun you wish to conjugate for:\n")

    isIrregular = checkIrregular(usrVerb, irregVerbs)
    endType = checkVerbEnd(usrVerb)
    print(isIrregular, endType)
    print(regularConj(usrPronoun, usrVerb, endType))



main()
