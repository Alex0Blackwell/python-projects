# Word Isolator

dontWant = ['(verb)']

verbFile = open('words/verbs.txt', 'r')
allVerbs = verbFile.readlines()
numLines = len(allVerbs)

for i in range(numLines):
    line = str(allVerbs[i])
    print(line.split()[0])
