with open(__file__[:-4] + ".txt") as file:
    points = set()
    for line in file:
        if line == "\n":
            break
        x, y = map(int, line.strip().split(","))
        points.add((x, y))

    for line in file:
        new_points = set()
        fold = line.strip().split("=")
        axis = fold[0][-1]
        value = int(fold[1])
        if axis == "x":
            for point in points:
                if point[0] > value:
                    new_points.add((2 * value - point[0], point[1]))
                else:
                    new_points.add(point)
        elif axis == "y":
            for point in points:
                if point[1] > value:
                    new_points.add((point[0], 2 * value - point[1]))
                else:
                    new_points.add(point)
        points = new_points
        break

    print(len(points))
