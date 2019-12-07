# Steps of an induction proof


def closeTarget(usrIn, target):
    # Check if what was inputted was probably right with maybe spelling
    # mistakes or improper formatting
    res = False
    minLen = min(len(usrIn), len(target))

    c = 0
    for i in range(minLen):
        if(usrIn[i] in target):
            c += 1

    if(c != 0 and c / len(target) > 0.9):
        # If over 90% of the characters from the user input match what
        # the target is, then it is probably charitably the right answer
        res = True

    return res


def main():
    firstStep = ''
    while(not closeTarget(firstStep, "State the base case")):
        firstStep = input("\nWhat is the first step to an inductive proof?:\n")
    print("Correct, first you need to state the base case. Only once the ",
          "base case is proven by a numerical test, can a proof for all",
          "numbers start.")

    secondStep = ''
    while(not closeTarget(secondStep, "Induction hypothesis")):
        secondStep = input("\nWhat is the second step to an inductive proof?:\n")
    print("Correct, you then need to let n = any arbitrary number k so we can",
          "prove for any number.")

    thirdStep = ''
    while(not closeTarget(thirdStep, "Inductive step")):
        thirdStep = input("\nWhat is the third step to an inductive proof?:\n")
    print("Correct, this is the step with most of the algebra where one side",
          "must equal the other side. Note that within this algebra, the",
          "inductive step will be used.")


main()
