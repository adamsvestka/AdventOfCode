with open(__file__[:-4] + ".txt") as file:
    scanners = []
    while file.readline():
        scanner = []
        while line := file.readline().strip():
            scanner.append(tuple(map(int, line.split(","))))
        scanners.append(scanner)

    add = lambda a, b: tuple(c + d for c, d in zip(a, b))
    sub = lambda a, b: tuple(c - d for c, d in zip(a, b))
    dist = lambda a, b: sum(i ** 2 for i in sub(a, b)) ** 0.5

    from itertools import combinations, permutations, product
    from collections import defaultdict
    from statistics import mode

    distmaps: dict[int, dict[int, tuple]] = {}
    for scanner, coords in enumerate(scanners):
        distmaps[scanner] = {dist(a, b): (i, j) for (i, a), (j, b) in combinations(enumerate(coords), 2)}

    indexmaps = {}
    for scanner1, scanner2 in combinations(distmaps, 2):
        beacons = defaultdict(list)
        for dist in distmaps[scanner1].keys() & distmaps[scanner2].keys():
            for index in distmaps[scanner1][dist]:
                beacons[index].extend(distmaps[scanner2][dist])

        common = {(k, mode(v)) for k, v in beacons.items() if len(v) > 2}
        if common:
            indexmaps[(scanner1, scanner2)] = common

    dupes = set()
    for (scanner1, scanner2), mappings in list(indexmaps.items()):
        dupes |= {(scanner2, j) for i, j in mappings}
        indexmaps[(scanner2, scanner1)] = {(j, i) for i, j in mappings}

    def combine(f, g):
        return lambda x: f(g(x))

    def dark_magic(points):
        for a, b, c in permutations(range(3)):
            for n1, n2, n3 in product([-1, 1], repeat=3):
                transform = lambda p: (n1 * p[a], n2 * p[b], n3 * p[c])
                distances = {sub(p1, transform(p2)) for p1, p2 in points}
                if len(distances) == 1:
                    (dist,) = distances
                    return lambda p, t=transform: add(t(p), dist)

    positions = {0: (0, 0, 0)}
    transformations = {0: lambda x: x}
    while len(scanners) != len(positions):
        for (scanner1, scanner2), mappings in indexmaps.items():
            if len(mappings) < 12:
                continue
            if scanner2 in positions or scanner1 not in positions:
                continue
            points = [(scanners[scanner1][i], scanners[scanner2][j]) for i, j in mappings]

            transformations[scanner2] = combine(transformations[scanner1], dark_magic(points))
            positions[scanner2] = transformations[scanner2]((0, 0, 0))

    res = max(map(lambda x: sum(map(abs, sub(positions[x[0]], positions[x[1]]))), combinations(positions, r=2)))
    print(res)
