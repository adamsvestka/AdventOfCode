with open(__file__[:-4] + ".txt") as file:
    grid = [[*map(int, line.strip())] for line in file]
    count = 0

    def flash(x, y):
        global count
        count += 1
        for dy in range(max(0, y - 1), min(y + 2, len(grid))):
            for dx in range(max(0, x - 1), min(x + 2, len(grid[dy]))):
                if dx != x or dy != y:
                    grid[dy][dx] += 1
                    if grid[dy][dx] == 10:
                        flash(dx, dy)

    for _ in range(100):
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                grid[y][x] += 1
                if grid[y][x] == 10:
                    flash(x, y)
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] >= 10:
                    grid[y][x] = 0

    print(count)
