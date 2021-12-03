def countAscendingListElems(lst: list):
    return len(list(filter(lambda x: x > 0 ,[j - i for i, j in zip(lst[: -1], lst[1:])])))

with open("../inputs/day1.txt") as file:
    data1 = [int(line) for line in file]

# Part 1 ===
    print("Part 1:", countAscendingListElems(data1))

# Part 2 ===
    data2 = [i + j + k for i, j, k in zip(data1[:-2],data1[1:-1], data1[2:])]
    print("Part 2:", countAscendingListElems(data2))

