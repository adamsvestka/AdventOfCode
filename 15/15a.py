with open(__file__[:-4] + ".txt") as file:
    grid = [[int(x) for x in [*line.strip()]] for line in file]

    from heapq import heappush, heappop

    heap = [(0, 0, 0)]
    seen = {(0, 0)}

    while heap:
        dist, x, y = heappop(heap)

        if x == len(grid) - 1 and y == len(grid[0]) - 1:
            print(dist)
            break

        for pos in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
            if pos[0] >= 0 and pos[0] < len(grid[0]) and pos[1] >= 0 and pos[1] < len(grid) and pos not in seen:
                heappush(heap, (dist + grid[pos[1]][pos[0]], *pos))
                seen.add(pos)
