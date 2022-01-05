with open(__file__[:-4] + ".txt") as file:
    bits = [0] * len(file.readline().strip())
    count = 0
    for line in file:
        for i, b in enumerate(line.strip()):
            if b == "1":
                bits[i] += 1
        count += 1
    gamma = 0
    for bit in bits:
        gamma <<= 1
        if bit > count / 2:
            gamma += 1
    epsilon = gamma ^ (1 << len(bits)) - 1
    print(gamma * epsilon)
