with open(__file__[:-4] + ".txt") as file:
    data = file.read().splitlines()
    grid = {(x, y): c for y, l in enumerate(data) for x, c in enumerate(l) if c in ">v"}
    height = len(data)
    width = len(data[0])

    def run():
        changed = False
        global grid
        new_grid = grid.copy()
        for x, y in list(grid.keys()):
            if grid.get((x, y)) == ">":
                if not grid.get(((x + 1) % width, y)):
                    del new_grid[(x, y)]
                    new_grid[((x + 1) % width, y)] = ">"
                    changed = True
        grid = new_grid.copy()
        for x, y in list(grid.keys()):
            if grid.get((x, y)) == "v":
                if not grid.get((x, (y + 1) % height)):
                    del new_grid[(x, y)]
                    new_grid[(x, (y + 1) % height)] = "v"
                    changed = True
        grid = new_grid
        return changed

    i = 1
    while run():
        i += 1

    print(i)
