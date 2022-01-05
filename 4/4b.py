with open(__file__[:-4] + ".txt") as file:
    draws = list(map(int, file.readline().split(",")))
    boards = []
    while file.readline():
        board = []
        for i in range(5):
            board.append(list(map(int, file.readline().split())))
        boards.append(board)

        def checkwin(boards, b):
            if len(boards) == 1:
                win(boards[0], number)
            boards.pop(b)

        def win(grid, n):
            s = 0
            for row in grid:
                for i in row:
                    if i != "x":
                        s += i
            print(s * n)
            exit()

    for number in draws:
        b = 0
        while b < len(boards):
            board = boards[b]
            for row in board:
                for i, n in enumerate(row):
                    if n == number:
                        row[i] = "x"
            for i in range(5):
                for j in range(5):
                    if board[i][j] != "x":
                        break
                else:
                    checkwin(boards, b)
                    b -= 1
                    break
                for j in range(5):
                    if board[j][i] != "x":
                        break
                else:
                    checkwin(boards, b)
                    b -= 1
                    break
            b += 1
