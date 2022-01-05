with open(__file__[:-4] + ".txt") as file:
    edges = {}
    for line in file:
        a, b = line.strip().split("-")
        if b != "start":
            if a not in edges:
                edges[a] = []
            edges[a].append(b)
        if a != "start":
            if b not in edges:
                edges[b] = []
            edges[b].append(a)

    def find(a, path, twice):
        if a == "end":
            yield path
            return
        for b in edges[a]:
            if b.islower() and b in path:
                if not twice:
                    yield from find(b, path + [b], True)
                continue
            yield from find(b, path + [b], twice)

    print(len(list(find("start", ["start"], False))))
