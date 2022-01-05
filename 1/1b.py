with open(__file__[:-4] + ".txt") as file:
    lines = file.readlines()
    incs = -1
    previous = 0
    for i in range(2, len(lines)):
        current = sum(map(int, lines[i - 2 : i + 1]))
        if current > previous:
            incs += 1
        previous = current
    print(incs)
