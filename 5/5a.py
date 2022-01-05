with open(__file__[:-4] + ".txt") as file:
    import re

    pipes = []
    size = (0, 0)
    for line in file:
        x1, y1, x2, y2 = map(int, re.match(r"(\d+),(\d+) -> (\d+),(\d+)", line).groups())
        pipes.append((x1, y1, x2, y2))
        size = (max(size[0], x1, x2), max(size[1], y1, y2))
    grid = [[0] * (size[0] + 1) for _ in range(size[1] + 1)]
    for x1, y1, x2, y2 in pipes:
        if x1 != x2 and y1 != y2:
            continue
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                grid[y][x] += 1
    crosses = 0
    for row in grid:
        for x in row:
            if x > 1:
                crosses += 1
    print(crosses)
