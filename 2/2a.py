with open(__file__[:-4] + ".txt") as file:
    horizontal = depth = 0
    for line in file:
        if line.startswith("forward"):
            horizontal += int(line.split()[1])
        elif line.startswith("up"):
            depth -= int(line.split()[1])
        elif line.startswith("down"):
            depth += int(line.split()[1])
    print(horizontal * depth)
