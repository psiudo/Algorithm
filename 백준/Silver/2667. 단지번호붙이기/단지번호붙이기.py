def dfs_stack(x, y):
    stack = [(x, y)]
    count = 0

    while stack:
        x, y = stack.pop()
        if grid[x][y] == 0:
            continue

        grid[x][y] = 0
        count += 1

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == 1:
                stack.append((nx, ny))

    return count

N = int(input())
grid = [list(map(int, input().strip())) for _ in range(N)]
result = []

for i in range(N):
    for j in range(N):
        if grid[i][j] == 1:
            result.append(dfs_stack(i, j))

print(len(result))
for count in sorted(result):
    print(count)