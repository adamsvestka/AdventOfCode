with open(__file__[:-4] + ".txt") as file:
    edges = {}
    for line in file:
        a, b = line.strip().split("-")
        if a not in edges:
            edges[a] = []
        edges[a].append(b)
        if b not in edges:
            edges[b] = []
        edges[b].append(a)

    def find(a, path):
        if a == "end":
            yield path
        for b in edges[a]:
            if b.islower() and b in path:
                continue
            yield from find(b, path + [b])

    print(len(list(find("start", ["start"]))))
