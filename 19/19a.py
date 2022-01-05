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

    from itertools import combinations
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
        indexmaps[(scanner2, scanner1)] = {(scanner2, index2) for index1, index2 in mappings}
        dupes |= indexmaps[(scanner2, scanner1)]

    count = sum(map(len, scanners)) - len(dupes)
    print(count)
