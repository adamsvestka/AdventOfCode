with open(__file__[:-4] + ".txt") as file:
    positions = [*map(int, file.read().split(","))]
    expenses = [0] * max(positions)
    for i in range(len(expenses)):
        for n in positions:
            d = abs(i - n)
            expenses[i] += d * (d + 1) // 2
    print(min(expenses))
