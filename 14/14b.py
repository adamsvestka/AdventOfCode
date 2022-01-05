with open(__file__[:-4] + ".txt") as file:
    from collections import Counter

    template = file.readline().strip()
    counter = Counter(zip(template, template[1:]))
    file.readline()
    pairs = dict([line.strip().split(" -> ") for line in file])

    for _ in range(40):
        for (a, b), c in list(counter.items()):
            counter[(a, b)] -= c
            counter[(a, pairs[a + b])] += c
            counter[(pairs[a + b], b)] += c

    res = Counter()
    for (a, b), c in counter.items():
        res[a] += c
        res[b] += c
    res[template[0]] += 1
    res[template[-1]] += 1

    print((res.most_common(1)[0][1] - res.most_common()[-1][1]) // 2)
