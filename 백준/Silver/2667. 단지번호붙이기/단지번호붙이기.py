N = int(input())
grid = [list(map(int, input())) for _ in range(N)]
#######################################
dv = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def bfs(x, y) :
    q = [(x, y)]
    cnt = 0

    while q :
        x, y = q.pop(0)

        # 방문여부
        if grid[x][y] == 0 :
            continue

        # 단지 수 추가 및 방문
        cnt += 1
        grid[x][y] = 0

        for dx, dy in dv :
            nx, ny = x + dx, y + dy
            if 0 <= nx <= N-1 and 0 <= ny <= N-1 and grid[nx][ny] != 0 :
                q.append((nx, ny))

    return cnt


#######################################
results = []
for x in range(N) :
    for y in range(N) :
        if grid[x][y] == 1 :
            results.append(bfs(x, y))


#######################################
print(len(results))
for result in sorted(results) :
    print(result)