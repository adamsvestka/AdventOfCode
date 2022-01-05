with open(__file__[:-4] + ".txt") as file:
    from ast import literal_eval
    from math import ceil
    from copy import deepcopy

    numbers = list(map(literal_eval, file))

    def add(a, b):
        number = [a, b]
        prev = None
        next = None
        coll = False
        state = False

        def traverse(node, depth=0):
            nonlocal prev, next, coll, state
            for i in range(len(node)):
                if state and depth >= 4 and isinstance(node[0], int) and isinstance(node[1], int) and next is None:
                    if prev:
                        prev[0][prev[1]] += node[0]
                    next = node[1]
                    coll = True
                    break
                if isinstance(node[i], list):
                    traverse(node[i], depth + 1)
                    if coll:
                        node[i] = 0
                        coll = False
                else:
                    if next is not None:
                        node[i] += next
                        raise ValueError("break")
                    if not state and node[i] >= 10:
                        node[i] = [node[i] // 2, ceil(node[i] / 2)]
                        raise ValueError("break")
                    prev = (node, i)

        def step(s):
            nonlocal prev, next, state
            # pprint(number)
            prev = next = None
            state = s
            try:
                traverse(number)
            except ValueError:
                return True

        while step(True) or step(False):
            pass

        return number

    def pprint(number):
        string = str(number)
        res = ""
        stack = []
        for i in range(len(string)):
            if string[i] == "[":
                stack.append(f"\x1b[3{len(stack) + 1}m")
                res += stack[-1]
            if string[i].isnumeric() and string[i + 1].isnumeric():
                res += f"\x1b[1;4m"
            res += string[i]
            if string[i - 1].isnumeric() and string[i].isnumeric():
                res += f"\x1b[0m"
                res += "".join(stack)
            if string[i] == "]":
                stack.pop()
                res += "\x1b[0m"
                res += "".join(stack)
        print(res + "\x1b[0m")

    def magnitude(node):
        if isinstance(node, list):
            return 3 * magnitude(node[0]) + 2 * magnitude(node[1])
        return node

    max = (0, None, None)
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                res = add(deepcopy(numbers[i]), deepcopy(numbers[j]))
                mag = magnitude(res)
                if mag > max[0]:
                    max = (mag, i, j)

    print(max[0])
