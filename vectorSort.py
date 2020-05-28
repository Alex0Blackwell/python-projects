def makeVector(array): #get max
    largest = array[0]

    for i in range(1, len(array)):
      if (array[i] > largest):
        largest = array[i]

    vector = [0]*(largest+1)
    for j in range(len(array)):
        vector[array[j]] += 1

    belowEqual = 0
    for k in range(len(vector)):
        belowEqual += vector[k]
        vector[k] = belowEqual

    # now sort (part b)----------------------------
    c = 0
    finalArray = [0]*len(array)

    last = 0
    for a in range(len(vector)):
        if(vector[a] > last):
            amountToAppend = vector[a] - last
            for add in range(amountToAppend):
                finalArray[c] = a
                c += 1
        last = vector[a]

    for el in finalArray:
      print(el)

def main():
    array = [3, 5, 2, 5, 4, 10, 3, 4, 5, 6, 1, 0]
    makeVector(array);

main()
