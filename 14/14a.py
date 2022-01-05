with open(__file__[:-4] + ".txt") as file:
    template = file.readline().strip()
    pairs = {}
    file.readline()

    for line in file:
        key, val = line.strip().split(" -> ")
        pairs[key] = val

    for _ in range(10):
        i = 0
        while i < len(template):
            key = template[i : i + 2]
            if key in pairs:
                template = template[: i + 1] + pairs[key] + template[i + 1 :]
                i += 1
            i += 1

    from collections import Counter

    c = Counter(template)
    print(c.most_common(1)[0][1] - c.most_common()[-1][1])
