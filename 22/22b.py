with open(__file__[:-4] + ".txt") as file:
    import re
    from collections import namedtuple
    from itertools import product

    Cuboid = namedtuple("Cuboid", "state, x1, x2, y1, y2, z1, z2")

    def create_instruction(line):
        n = r"(-?\d+)"
        state, *rest = re.search(rf"^(on|off) x={n}..{n},y={n}..{n},z={n}..{n}$", line).groups()
        return Cuboid(1 if state == "on" else -1, *map(int, rest))

    instructions = [create_instruction(line) for line in file]

    def intersect(c1: Cuboid, c2: Cuboid):
        if c1.x1 > c2.x2 or c1.x2 < c2.x1:
            return False
        if c1.y1 > c2.y2 or c1.y2 < c2.y1:
            return False
        if c1.z1 > c2.z2 or c1.z2 < c2.z1:
            return False

        x1 = max(c1.x1, c2.x1)
        x2 = min(c1.x2, c2.x2)
        y1 = max(c1.y1, c2.y1)
        y2 = min(c1.y2, c2.y2)
        z1 = max(c1.z1, c2.z1)
        z2 = min(c1.z2, c2.z2)

        state = -c1.state if c1.state == c2.state else c1.state
        return Cuboid(state, x1, x2, y1, y2, z1, z2)

    def volume(c: Cuboid):
        return (c.x2 - c.x1 + 1) * (c.y2 - c.y1 + 1) * (c.z2 - c.z1 + 1) * c.state

    cubes = []
    for inst in instructions:
        intersections = [*filter(None, [intersect(inst, c) for c in cubes])]
        cubes.extend(intersections)
        if inst.state == 1:
            cubes.append(inst)

    res = sum(volume(cube) for cube in cubes)
    print(res)
