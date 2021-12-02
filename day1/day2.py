from functools import reduce

with open("../inputs/day2.txt") as file:
    dataAsStrings = [(line.strip()).split() for line in file]
    directions, numbers = zip(*dataAsStrings)

    valueList = list(zip(directions, list(map(int, numbers))))

# Part 1 ===
    depth,dist = reduce(
        lambda status, x: (status[0] + x[1], status[1]) if x[0] == 'down' else ( (status[0] - x[1], status[1]) if x[0] == 'up' else (status[0], status[1] + x[1]) ),
        valueList, (0,0))

    print('Part 1:', depth * dist)


# Part 2 ===
    depth,_,dist = reduce(
        lambda status, x: (status[0], status[1] + x[1], status[2]) if x[0] == 'down' else
            ((status[0], status[1] - x[1], status[2]) if x[0] == 'up' else (status[0] + status[1] * x[1], status[1], status[2] + x[1])),
            valueList,
            (0, 0, 0))

    print('Part 2:', depth*dist)