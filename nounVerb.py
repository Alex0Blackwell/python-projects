# Select the nouns and verbs in a sentence


def testWord(word, nouns, verbs):
    (verifyN, verifyV) = False, False
    if(word in nouns):
        (verifyN, verifyV) = True, False
    elif(word in verbs):
        (verifyN, verifyV) = False, True
    elif(word.lower() == 'alexandra'):
        print('Oh your sentence has the word \"Alexandra\", I love Alexandra')
    return (verifyN, verifyV)


def cleanWords(wordLst):
    res = []
    for i in range(len(wordLst)):
        clean = ''
        for char in wordLst[i]:
            if char.isalpha():
                clean += char
        res += [clean.lower()]
    return res


def main():
    allNouns = []
    allVerbs = []
    nouns = []
    verbs = []

    nounFile = open('words/nouns.txt', 'r')
    allNouns = nounFile.read().splitlines()
    nounFile.close()

    verbFile = open('words/verbs.txt', 'r')
    allVerbs = verbFile.read().splitlines()
    verbFile.close()

    sentence = (input("Enter a sentence and I'll tell you"
                "the nouns and verbs!\n"))
    wordSep = sentence.split()
    wordsClean = cleanWords(wordSep)

    for i in range(len(wordSep)):
        (n, v) = False, False
        tense = ''

        if(wordsClean[i][-3:] == 'ing'):
            (n, v) = testWord(wordsClean[i][:-3], allNouns, allVerbs)
            tense = ' (present tense)'
        elif(wordsClean[i][-2:] == 'ed'):
            (n, v) = testWord(wordsClean[i][:-2], allNouns, allVerbs)
            tense = ' (past tense)'
        else:
            (n, v) = testWord(wordsClean[i], allNouns, allVerbs)

        if(n):
            nouns += [wordSep[i] + tense]
        if(v):
            verbs += [wordSep[i] + tense]

    print(f"Nouns:\n{nouns}")
    print(f"Verbs:\n{verbs}")


main()
