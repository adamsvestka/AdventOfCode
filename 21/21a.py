with open(__file__[:-4] + ".txt") as file:
    import re
    players = [int(re.search(r'Player (\d+) starting position: (\d+)', line).group(2)) for line in file]
    scores = [0] * len(players)

    current = 0
    def roll():
        global current
        current += 1
        return (current - 1) % 100 + 1

    turn = 0
    while True:
        players[turn] = (players[turn] + sum([roll() for _ in range(3)]) - 1) % 10 + 1
        scores[turn] += players[turn]
        if scores[turn] >= 1000:
            break
        turn = (turn + 1) % len(players)

    print(current * scores[1 - turn])
