from collections import deque


def num_of_islands_in_border(grid: list[list[int]]):
    if not grid:
        return

    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0

    def bfs(r, c):
        q = deque()
        visited.add((r, c))
        q.append((r, c))
        x = 0
        while q:
            row, col = q.popleft()
            if (row == 0 or
                col == 0 or
                row == rows-1 or
                    col == cols-1):
                x = 1
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                i, j = row + dr, col + dc
                if (0 <= i < rows and
                    0 <= j < cols and
                    grid[i][j] == 1 and
                        (i, j) not in visited):
                    q.append((i, j))
                    visited.add((i, j))
        return x
    for r in range(rows):  # O(n)
        for c in range(cols):  # O(n)
            if grid[r][c] == 1 and (r, c) not in visited:
                islands += bfs(r, c)  # O(n)

    return islands


print(num_of_islands_in_border([
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
]))
