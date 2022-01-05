with open(__file__[:-4] + ".txt") as file:
    positions = [*map(int, file.read().split(","))]
    expenses = [0] * max(positions)
    for i in range(len(expenses)):
        for n in positions:
            expenses[i] += abs(i - n)
    print(min(expenses))
