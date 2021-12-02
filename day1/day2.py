from functools import reduce


def countAscendingListElems(lst: list):
    return len(list(filter(lambda x: x > 0 ,[j - i for i, j in zip(lst[: -1], lst[1:])])))
def sumKeyValuesZippedList(lst: list, key:str):
    return sum([w2 for (w1,w2) in  lst if w1 == key])

with open("../inputs/day2.txt") as file:
    dataAsStrings = [(line.strip()).split() for line in file]
    directions, numbers = zip(*dataAsStrings)

    valueList = list(zip(directions, list(map(int, numbers))))

# Part 1 ===
    downSum = sumKeyValuesZippedList(valueList, 'down')
    forwardSum  = sumKeyValuesZippedList(valueList, 'forward')
    upSum  = sumKeyValuesZippedList(valueList, 'up')
    print('Part 1:', (downSum - upSum) * forwardSum)

# Part 2 ===
    depth = aim = dist = 0
    for direction, value in valueList:
        if direction == 'down':
            aim += value
        elif direction == 'up':
            aim -= value
        elif direction == 'forward':
            dist += value
            depth += aim*value

    print('Part 2:', depth*dist)




