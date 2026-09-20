factory = [
    ['S', '.', '#', '.', '.', '.'],
    ['.', '.', '#', '.', '#', '.'],
    ['#', '.', '.', '.', '#', '.'],
    ['.', '#', '.', '#', '.', '.'],
    ['.', '.', '.', '#', '.', '.'],
    ['.', '#', '.', '.', '.', 'G']
]

for row in factory:
    print(row)


from collections import deque

def bfs(factory):
    rows = len(factory)
    cols = len(factory[0])

    # Find the starting position S
    for i in range(rows):
        for j in range(cols):
            if factory[i][j] == 'S':
                start = (i, j)

    queue = deque([start])
    visited = {start}
    nodes_explored = 0

    while queue:
        current = queue.popleft()
        nodes_explored += 1

        row, col = current

        # Check if goal G is found
        if factory[row][col] == 'G':
            return nodes_explored

        # Up, Down, Left, Right
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc

            if (0 <= new_row < rows and
                0 <= new_col < cols and
                factory[new_row][new_col] != '#' and
                (new_row, new_col) not in visited):

                visited.add((new_row, new_col))
                queue.append((new_row, new_col))

    return nodes_explored


nodes = bfs(factory)
print("BFS nodes explored:", nodes)

def dfs(factory):
    rows = len(factory)
    cols = len(factory[0])

    # Find the starting position S
    for i in range(rows):
        for j in range(cols):
            if factory[i][j] == 'S':
                start = (i, j)

    stack = [start]
    visited = {start}
    nodes_explored = 0

    while stack:
        current = stack.pop()
        nodes_explored += 1

        row, col = current

        # Check if goal G is found
        if factory[row][col] == 'G':
            return nodes_explored

        # Up, Down, Left, Right
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc

            if (0 <= new_row < rows and
                0 <= new_col < cols and
                factory[new_row][new_col] != '#' and
                (new_row, new_col) not in visited):

                visited.add((new_row, new_col))
                stack.append((new_row, new_col))

    return nodes_explored


nodes_dfs = dfs(factory)
print("DFS nodes explored:", nodes_dfs)

import time

repetitions = 10000

print("\nBFS Timing:")

for run in range(3):
    start_time = time.perf_counter()

    for i in range(repetitions):
        bfs(factory)

    end_time = time.perf_counter()

    total_time = end_time - start_time

    print("Run", run + 1, ":", total_time * 1000, "ms for",
          repetitions, "BFS runs")


print("\nDFS Timing:")

for run in range(3):
    start_time = time.perf_counter()

    for i in range(repetitions):
        dfs(factory)

    end_time = time.perf_counter()

    total_time = end_time - start_time

    print("Run", run + 1, ":", total_time * 1000, "ms for",
          repetitions, "DFS runs")