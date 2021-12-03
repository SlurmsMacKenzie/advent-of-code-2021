def getGamma(lst: list):
    gamma = 0
    for i in range(0,12):
        gamma += pow(2,i)*getMostCommonBinDigitAt(lst, i)

    return gamma

def getEpsilon(lst: list):
    epsilon = 0
    for i in range(0,12):
        epsilon += pow(2,i)*getLeastCommonBinDigitAt(lst, i)

    return epsilon

def getOxygenValue(lst:list):
    itList = lst
    index = 11
    while len(itList) > 1:
        mostCommonBit = getMostCommonBinDigitAt(itList, index)
        itList = [ elem for elem in itList if (elem//pow(2,index)) % 2 == mostCommonBit]
        index -= 1
    return itList[0]

def getCO2Value(lst:list):
    itList = lst
    index = 11
    while len(itList) > 1:
        leastCommonBit = getLeastCommonBinDigitAt(itList, index)
        itList = [ elem for elem in itList if (elem//pow(2,index)) % 2 == leastCommonBit]
        index -= 1
    return itList[0]

def getMostCommonBinDigitAt(lst:list, n:int):
    return 1 if sum([ (i//pow(2,n)) % 2  for i in lst])/len(lst) >= 0.5 else 0

def getLeastCommonBinDigitAt(lst:list, n:int):
    return 0 if sum([ (i//pow(2,n)) % 2  for i in lst])/len(lst) >= 0.5 else 1

with open("../inputs/day3.txt") as file:
    numbers = [int(line , 2) for line in file]

# Part 1 ===
    print('Part 1:', getEpsilon(numbers)*getGamma(numbers) )


# Part 2 ===
    print('Part 2:', getOxygenValue(numbers)*getCO2Value(numbers))