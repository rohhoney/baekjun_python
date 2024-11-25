string = input()

stringLen = len(string)
setA = set()

for i in range (0, stringLen):
    for ii in range(0, stringLen - i):
        setA.add(string[i: i + 1 + ii])


print(len(setA))
