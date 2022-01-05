with open(__file__[:-4] + ".txt") as file:
    from collections import deque

    s = lambda x: ")]}>"["([{<".index(x)]
    scores = []
    for line in file:
        front = deque()
        for c in line.strip():
            if c in "([{<":
                front.append(c)
            else:
                if c != s(front.pop()):
                    break
        else:
            if len(front):
                score = 0
                for c in reversed(front):
                    score *= 5
                    score += "([{<".index(c) + 1
                scores.append(score)
    print(sorted(scores)[len(scores) // 2])
