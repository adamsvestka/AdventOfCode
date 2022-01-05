with open(__file__[:-4] + ".txt") as file:
    incs = -1
    previous = 0
    for line in file:
        current = int(line)
        if current > previous:
            incs += 1
        previous = current
    print(incs)
