with open(__file__[:-4] + ".txt") as file:
    grid = [*map(lambda x: [*map(int, [*x.strip()])], file.readlines())]

    def basin(x, y):
        size = 1
        grid[y][x] = 9
        if x > 0 and grid[y][x - 1] != 9:
            size += basin(x - 1, y)
        if x < len(grid[y]) - 1 and grid[y][x + 1] != 9:
            size += basin(x + 1, y)
        if y > 0 and grid[y - 1][x] != 9:
            size += basin(x, y - 1)
        if y < len(grid) - 1 and grid[y + 1][x] != 9:
            size += basin(x, y + 1)
        return size

    basins = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] != 9:
                basins.append(basin(x, y))

    from math import prod

    print(prod(sorted(basins)[-3:]))
