# what should study
# based on what you're stressed about and how you suck at the subject


def calculateStudy(data):
    total = []
    for i in range(len(data)):
        total += [(data[i][0], data[i][1] + data[i][2])]
    return total


def main():
    subjects = []
    subjectData = []
    subjectNum = int(input("How many courses do you have?\n"))

    for a in range(subjectNum):
        subject = input(f"name your {a+1} subject:\n")
        subjects.append(subject)

    for b in range(subjectNum):
        stress = int(input(f"How stressed are you about {subjects[b]} /10?\n"))
        suck = int(input(f"How much do you suck at {subjects[b]} /10\n"))
        subjectData += [[subjects[b], stress, suck]]

    addStressSuck = calculateStudy(subjectData)
    subjectSorted = sorted(addStressSuck, key=lambda tup: tup[1], reverse=True)

    for c in range(len(subjectSorted)):
        beg = '... and then'
        if(c == 0):
            beg = "Ok, first"
        print(f"{beg} you should study {subjectSorted[c][0]}")


main()
