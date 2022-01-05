with open(__file__[:-4] + ".txt") as file:
    initial = [*map(int, file.read().split(","))]
    counts = [0] * 9
    for i in initial:
        counts[i] += 1
    for _ in range(80):
        spawn = counts[0]
        for i in range(1, len(counts)):
            counts[i - 1] = counts[i]
        counts[6] += spawn
        counts[8] = spawn
    print(sum(counts))
