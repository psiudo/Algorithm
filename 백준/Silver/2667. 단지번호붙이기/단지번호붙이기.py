def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= N or grid[x][y] == 0:
        return 0

    grid[x][y] = 0
    count = 1

    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        count += dfs(x + dx, y + dy)

    return count

N = int(input())
grid = [list(map(int, list(input()))) for _ in range(N)]
result = []

for i in range(N):
    for j in range(N):
        if grid[i][j] == 1:
            result.append(dfs(i, j))

print(len(result))
for count in sorted(result):
    print(count)