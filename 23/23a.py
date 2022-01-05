with open(__file__[:-4] + ".txt") as file:
    data = "".join([c for row in file.read().split() for c in row if c != "#"])

    # 0 1 2 3 4 5 6 7 8 9 10
    #    11  12  13  14
    #    15  16  17  18

    valid = [0, 1, 3, 5, 7, 9, 10]
    doors = {
        "A": 2,
        "B": 4,
        "C": 6,
        "D": 8,
    }
    destinations = {
        "A": [11, 15],
        "B": [12, 16],
        "C": [13, 17],
        "D": [14, 18],
    }

    def cost(a):
        return 10 ** "ABCD".index(a)

    from collections import namedtuple

    Move = namedtuple("Move", "fron, to, steps")

    def generate_moves(board):
        for i in valid:
            if board[i] != ".":
                a = board[i]
                dest = destinations[a]
                x, y = (doors[a], i) if doors[a] < i else (i + 1, doors[a] + 1)
                if all(board[j] == "." for j in range(x, y)) and all(board[j] in "." + a for j in dest):
                    for j in range(len(dest)):
                        if board[dest[j]] != ".":
                            j -= 1
                            break
                    yield Move(i, dest[j], j + 1 + y - x)
        for A in destinations.keys():
            for i in destinations[A]:
                if board[i] == ".":
                    continue
                if not all(board[j] == "." for j in destinations[A] if j < i):
                    continue
                door = doors[A]
                for j in range(door, -1, -1):
                    if board[j] != ".":
                        break
                    if j in valid:
                        yield Move(i, j, destinations[A].index(i) + 1 + door - j)
                for j in range(door, 11):
                    if board[j] != ".":
                        break
                    if j in valid:
                        yield Move(i, j, destinations[A].index(i) + 1 + j - door)

    def run(move: Move, board: str):
        board = list(board)
        a = board[move.fron]
        board[move.fron] = "."
        board[move.to] = a
        return ("".join(board), move.steps * cost(a))

    from heapq import heappush, heappop

    def simulate(board):
        queue = [(0, board)]
        seen = {board: 0}
        target = "." * 11 + "ABCD" * 2
        while queue:
            cost, state = heappop(queue)
            if state == target:
                return cost
            for move in generate_moves(state):
                new_state, new_cost = run(move, state)
                new_cost += cost
                if new_state in seen and seen[new_state] <= new_cost:
                    continue
                seen[new_state] = new_cost
                heappush(queue, (new_cost, new_state))

    res = simulate(data)
    print(res)
