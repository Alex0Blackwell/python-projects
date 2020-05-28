def main():
  dupArr = []

  usrIn = input("input: ")

  # get largest num that divides twice
  divide = 1
  c = 1
  while(divide >= 1):
    divide = (len(usrIn)-1)/2 / c
    c += 1
  c -= 1
  print(c)

   # now we have the largest num that we can use
  subStrLen = 1
  for a in range(c):
    # increment our substring len
    for b in range(len(usrIn)):
      # for each letter
      for c in range(b+subStrLen, len(usrIn)-b-subStrLen, subStrLen):
        print(f"{usrIn[b:b-1+subStrLen]} and {usrIn[c-subStrLen:c]}")
        if(usrIn[b-1:b-1+subStrLen] == usrIn[c-subStrLen:c]):
          dupArr += usrIn[c-subStrLen:c]
    subStrLen += 1


  print("dupArr: ", dupArr)


main()
