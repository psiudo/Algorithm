from collections import deque

def bfs(grid, x, y, H, W, visited):
    # 방향 벡터: 상, 하, 좌, 우
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and grid[nx][ny] == '#':
                visited[nx][ny] = True
                queue.append((nx, ny))

def solve():
    T = int(input().strip())
    for _ in range(T):
        H, W = map(int, input().strip().split())
        grid = [list(input().strip()) for _ in range(H)]
        visited = [[False] * W for _ in range(H)]
        sheep_count = 0

        for i in range(H):
            for j in range(W):
                if grid[i][j] == '#' and not visited[i][j]:
                    bfs(grid, i, j, H, W, visited)
                    sheep_count += 1

        print(sheep_count)

if __name__ == "__main__":
    solve()
