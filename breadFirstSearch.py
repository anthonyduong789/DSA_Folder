from collections import deque

matrix = [
    [1, 1, 0, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 2, 1, 1],  # Let's say we're looking for the '2'
    [0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1]
]

start = (2, 0)  # Start left side (not on the 2)
target_value = 2

def bfs_find(matrix, start, target_value):
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue = deque()
    queue.append((start[0], start[1], 0))  # (row, col, distance)
    visited[start[0]][start[1]] = True

    directions = [(-1,0), (1,0), (0,-1), (0,1)]  # Up, Down, Left, Right

    while queue:
        r, c, dist = queue.popleft()
        print(f"Visiting ({r},{c}) at distance {dist}")

        if matrix[r][c] == target_value:
            print(f"Found target at ({r},{c}) in {dist} steps!")
            return dist

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] != 0 and not visited[nr][nc]:
                queue.append((nr, nc, dist + 1))
                visited[nr][nc] = True

    print("Target not found.")
    return -1  # If not found


if __name__ == "__main__":
    print(bfs_find(matrix, start, target_value))


