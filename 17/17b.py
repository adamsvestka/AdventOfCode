with open(__file__[:-4] + ".txt") as file:
    import re
    from math import ceil

    x1, x2, y1, y2 = map(int, re.search("target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)", file.read()).groups())

    ymax = -y1 - 1
    ymin = y1
    xmax = x2
    xmin = ceil(-0.5 + (0.25 + 2 * x1) ** 0.5)

    def test(vx, vy):
        x = y = 0
        while x <= x2 and y >= y1:
            if x >= x1 and y <= y2:
                return True
            x += vx
            y += vy
            if vx:
                vx += -1 if vx > 0 else 1
            vy -= 1
        return False

    count = 0
    for x in range(xmin, xmax + 1):
        for y in range(ymin, ymax + 1):
            if test(x, y):
                count += 1
    print(count)
