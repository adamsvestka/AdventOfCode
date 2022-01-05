with open(__file__[:-4] + ".txt") as file:
    import re

    x1, x2, y1, y2 = map(int, re.search("target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)", file.read()).groups())

    n = -y1 - 1
    print(n * (n + 1) // 2)
