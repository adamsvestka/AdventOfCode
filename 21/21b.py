with open(__file__[:-4] + ".txt") as file:
    import re
    from collections import namedtuple
    from itertools import product

    p = tuple(int(re.search(r"Player (\d+) starting position: (\d+)", line).group(2)) for line in file)

    Universe = namedtuple("Universe", "players, scores, turn")
    universes = {Universe(p, (0, 0), 0): 1}

    moves = {}
    for i in product([1, 2, 3], repeat=3):
        n = sum(i)
        if n not in moves:
            moves[n] = 0
        moves[n] += 1

    wins = [0, 0]
    while universes:
        for (players, scores, turn), count in sorted(universes.items()):
            del universes[Universe(players, scores, turn)]
            for roll, times in moves.items():
                new_players = list(players)
                new_players[turn] = (new_players[turn] + roll - 1) % 10 + 1

                new_scores = list(scores)
                new_scores[turn] += new_players[turn]

                new_turn = (turn + 1) % 2
                new_uni = Universe(tuple(new_players), tuple(new_scores), new_turn)
                new_count = count * times

                if new_uni.scores[turn] >= 21:
                    wins[turn] += new_count
                    continue

                universes[new_uni] = universes.get(new_uni, 0) + new_count

    print(max(wins))
