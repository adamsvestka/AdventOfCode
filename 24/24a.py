with open(__file__[:-4] + ".txt") as file:
    program = file.read().splitlines()

    from collections import namedtuple

    Block = namedtuple("Block", "pop, a, b")

    blocks: list[Block] = []
    for i in range(0, len(program), 18):
        get = lambda x: int(program[i + x].split()[-1])
        blocks.append(Block(get(4) != 1, get(5), get(15)))

    def run(number):
        stack = []

        for i, w in enumerate(map(int, str(number))):
            block = blocks[i]
            if stack != []:
                x = stack[-1]
                if block.pop:
                    stack.pop()
            else:
                x = 0
            if x + block.a != w:
                stack.append(w + block.b)

        return stack

    restraints = []
    stack = []
    for i, block in enumerate(blocks):
        if not block.pop:
            stack.append((block.b, i))
        else:
            head = stack.pop()
            restraints.append((i, head[1], head[0] + block.a))

    result = [0] * 14
    for rest in restraints:
        right_input = min(9, 9 - rest[2])
        left_input = right_input + rest[2]
        result[rest[0]] = left_input
        result[rest[1]] = right_input

    res = "".join(map(str, result))
    print(res)
