# Select the nouns and verbs in a sentence

allNouns = []
allVerbs = []
nouns = []
verbs = []

verbFile = open('words/verbs.txt', 'r')
rawVerbs = verbFile.readlines()
lenV = len(rawVerbs)
verbFile.close()

for a in range(lenV):
    allVerbs += [rawVerbs[a].rstrip()]


nounFile = open('words/nouns.txt', 'r')
rawNouns = nounFile.readlines()
lenN = len(rawNouns)
nounFile.close()

for b in range(lenN):
    allNouns += [rawNouns[b].rstrip()]


sentence = input("Enter a sentence and I'll tell you the nouns and verbs!\n")
wordSep = sentence.split()

def testWord(word):
    (verifyN, verifyV) = False, False
    if(word in allNouns):
        (verifyN, verifyV) = True, False
    elif(word in allVerbs):
        (verifyN, verifyV) = False, True
        return (verifyN, verifyV)



for i in range(len(wordSep)):
    (n, v) = False, False
    print(wordSep[i][:-3])
    if(wordSep[i][-3:] == 'ing'):
        res = testWord(wordSep[i][:-3])
        print(f"returns: {res}")
        (n, v) = testWord(wordSep[i][:-3])
    else:
        (n, v) = testWord(wordSep[i])

    if(n):
        nouns += [wordSep[i]]
    if(v):
        verbs += [wordSep[i]]

    # if(wordSep[i] in allNouns):
    #     nouns += [wordSep[i]]
    # elif(wordSep[i] in allVerbs):
    #     verbs += [wordSep[i]]


print(f"Nouns:\n{nouns}")
print(f"Verbs:\n{verbs}")
