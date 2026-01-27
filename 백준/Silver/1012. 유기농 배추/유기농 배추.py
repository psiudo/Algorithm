def dfs(x, y):
    stack = [(x, y)]

    while stack:
        x, y = stack.pop()

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0<= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and farm[nx][ny] == 1:
                stack.append((nx, ny))
                visited[nx][ny] = 1


T = int(input())

for ts in range(1, T + 1):
    M, N, K = map(int, input().split())
    farm = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    count = 0

    for _ in range(K):
        x, y = map(int, input().split())
        farm[y][x] = 1

    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1 and visited[i][j] == 0:
                count += 1
                dfs(i, j)

    print(count)