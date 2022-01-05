with open(__file__[:-4] + ".txt") as file:
    points = set()
    size = (0, 0)

    for line in file:
        if line == "\n":
            break
        x, y = map(int, line.strip().split(","))
        points.add((x, y))
        size = (max(size[0], x), max(size[1], y))

    for line in file:
        new_points = set()
        fold = line.strip().split("=")
        axis = fold[0][-1]
        value = int(fold[1])
        if axis == "x":
            size = (size[0] // 2, size[1])
            for point in points:
                if point[0] > value:
                    new_points.add((2 * value - point[0], point[1]))
                else:
                    new_points.add(point)
        elif axis == "y":
            size = (size[0], size[1] // 2)
            for point in points:
                if point[1] > value:
                    new_points.add((point[0], 2 * value - point[1]))
                else:
                    new_points.add(point)
        points = new_points

    board = [["."] * size[0] for _ in range(size[1])]
    for point in points:
        board[point[1]][point[0]] = "#"

    for row in board:
        print("".join(row))
