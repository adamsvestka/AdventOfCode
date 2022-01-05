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
        x = 0 if x1 == x2 else (x1 - x2) // abs(x1 - x2)
        y = 0 if y1 == y2 else (y1 - y2) // abs(y1 - y2)
        d = abs(x1 - x2 if x else y1 - y2)
        for i in range(d + 1):
            grid[y2 + i * y][x2 + i * x] += 1
    crosses = 0
    for row in grid:
        for x in row:
            if x > 1:
                crosses += 1
    print(crosses)
