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
    verbChange = verb[:-2]

    if(pro == 'je'):
        if(ir):
            verbChange += 'is'
        elif(re):
            verbChange += 's'
        elif(er):
            verbChange += 'e'
    elif(pro == 'tu'):
        if(ir):
            verbChange += 'is'
        elif(re):
            verbChange += 's'
        elif(er):
            verbChange += 'es'
    elif(pro == 'il' or pro == 'elle' or pro == 'on'):
        if(ir):
            verbChange += 'it'
        elif(re):
            pass
        elif(er):
            verbChange += 'e'
    elif(pro == 'nous'):
        if(ir):
            verbChange += 'issons'
        elif(re):
            verbChange += 'ons'
        elif(er):
            verbChange += 'ons'
    elif(pro == 'vous'):
        if(ir):
            verbChange += 'issez'
        elif(re):
            verbChange += 'ez'
        elif(er):
            verbChange += 'ez'
    elif(pro == 'ils' or pro == 'elles'):
        if(ir):
            verbChange += 'issent'
        elif(re):
            verbChange += 'ent'
        elif(er):
            verbChange += 'ent'
    else:
        verbChange = False

    return verbChange


def main():
    irregFile = open("irregularVerbs.txt", "r")
    irregVerbs = irregFile.read().splitlines()
    irregFile.close()

    usrVerb = input("Enter the French verb you wish to conjugate:\n")
    usrPronoun = input("Enter the pronoun you wish to conjugate for:\n")

    endType = checkVerbEnd(usrVerb)

    while(endType == (False, False, False) and usrVerb != 'e'):
        usrVerb = input(f'''You inputted {usrVerb} which ends with, {usrVerb[-2:]}
Only verbs ending with \"-ir\", \"-er\", or \"-ir\" can be converted.
Try again with a revised verb or type \"e\" to exit:\n''')
        endType = checkVerbEnd(usrVerb)

    isIrregular = checkIrregular(usrVerb, irregVerbs)
    conjdVerb = regularConj(usrPronoun, usrVerb, endType)
    endsWith = usrVerb[-2:]

    if(not(isIrregular)):
        print(f"The verb to conjugate was {usrVerb}.\nThe pronoun to",
              f"conjugate it with was {usrPronoun}.\nSince the verb is not",
              f"irregular, and it ends with {endsWith}, the conjugated verb",
              f"is:\n{conjdVerb}")
    else:
        print(f"The verb to conjugate was {usrVerb}.\nHowever, this is an",
              f"irregular verb and I'm only in CMPT 120\nso this seems like a",
              f"question for the internet.")


main()
