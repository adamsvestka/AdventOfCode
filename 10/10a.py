with open(__file__[:-4] + ".txt") as file:
    from collections import deque

    illegal = {")": 0, "]": 0, "}": 0, ">": 0}
    scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
    for line in file:
        front = deque()
        for c in line.strip():
            if c in "([{<":
                front.append(c)
            else:
                if c != ")]}>"["([{<".index(front.pop())]:
                    illegal[c] += 1
                    break
    score = 0
    for c in illegal:
        score += illegal[c] * scores[c]
    print(score)
