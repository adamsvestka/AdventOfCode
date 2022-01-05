with open(__file__[:-4] + ".txt") as file:
    import re
    from collections import namedtuple
    from itertools import product

    Instruction = namedtuple("Instruction", "state, x, y, z")

    def create_instruction(line):
        n = r"(-?\d+)"
        state, x1, x2, y1, y2, z1, z2 = re.search(rf"^(on|off) x={n}..{n},y={n}..{n},z={n}..{n}$", line).groups()
        bound = lambda f, t: range(max(int(f), -50), min(int(t), 50) + 1)
        return Instruction(int(state == "on"), bound(x1, x2), bound(y1, y2), bound(z1, z2))

    instructions = [create_instruction(line) for line in file]

    dim = 50
    size = 2 * dim + 1
    box = [[[0 for _ in range(size)] for _ in range(size)] for _ in range(size)]

    for inst in instructions:
        for x, y, z in product(inst.x, inst.y, inst.z):
            box[dim + x][dim + y][dim + z] = inst.state

    count = sum(sum(sum(row) for row in box) for box in box)
    print(count)
