with open(__file__[:-4] + ".txt") as file:
    grid = [*map(lambda x: [*map(int, [*x.strip()])], file.readlines())]
    points = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] < min(
                grid[y - 1][x] if y > 0 else 9,
                grid[y][x - 1] if x > 0 else 9,
                grid[y][x + 1] if x < len(grid[y]) - 1 else 9,
                grid[y + 1][x] if y < len(grid) - 1 else 9,
            ):
                points.append((x, y))
    score = 0
    for point in points:
        score += grid[point[1]][point[0]] + 1
    print(score)
