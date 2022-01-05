with open(__file__[:-4] + ".txt") as file:
    mapping = file.readline().strip()
    file.readline()
    board = [list(line.strip()) for line in file]

    if mapping[0] == "#" and mapping[-1] == "#":
        print(float("inf"))
        exit()

    from itertools import product

    def enhance(board, i):
        f = "." if i % 2 == 0 else "#"
        new_board = [[f] * (len(board[0]) + 2)] + [[f] + line + [f] for line in board] + [[f] * (len(board[0]) + 2)]
        for y in range(-1, len(board) + 1):
            for x in range(-1, len(board[0]) + 1):
                num = 0
                for i, j in product((-1, 0, 1), repeat=2):
                    num <<= 1
                    if y + i >= 0 and y + i < len(board) and x + j >= 0 and x + j < len(board[0]):
                        num += board[y + i][x + j] == "#"
                    elif mapping[0] == "#" and f == "#":
                        num += 1
                new_board[y + 1][x + 1] = mapping[num]
        return new_board

    for i in range(2):
        board = enhance(board, i)

    count = sum(sum(line.count("#") for line in board) for board in board)
    print(count)
