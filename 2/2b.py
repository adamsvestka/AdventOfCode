with open(__file__[:-4] + ".txt") as file:
    horizontal = depth = aim = 0
    for line in file:
        x = int(line.split()[1])
        if line.startswith("forward"):
            horizontal += x
            depth += aim * x
        elif line.startswith("up"):
            aim -= x
        elif line.startswith("down"):
            aim += x
    print(horizontal * depth)
