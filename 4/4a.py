with open(__file__[:-4] + ".txt") as file:
    draws = list(map(int, file.readline().split(",")))
    boards = []
    while file.readline():
        board = []
        for i in range(5):
            board.append(list(map(int, file.readline().split())))
        boards.append(board)

        def win(grid, n):
            s = 0
            for row in grid:
                for i in row:
                    if i != "x":
                        s += i
            print(s * n)
            exit()

    for number in draws:
        for board in boards:
            for row in board:
                for i, n in enumerate(row):
                    if n == number:
                        row[i] = "x"
            for i in range(5):
                for j in range(5):
                    if board[i][j] != "x":
                        break
                else:
                    win(board, number)
                for j in range(5):
                    if board[j][i] != "x":
                        break
                else:
                    win(board, number)
