from collections import deque

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# find 2 source
viruses = []
for x in range(N) :
    for y in range(M) :
        if grid[x][y] == 2 :
            viruses.append((x, y))

def bfs(viruses):
    v = [[0] * M for _ in range(N)] # 오염되지 않도록 매번 갱신
    # 감염처리
    for x, y in viruses :
        v[x][y] = 1
    q = deque(viruses)
    while q :
        x, y = q.popleft()

        for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)] :
            nx, ny = x + dx, y + dy
            if 0 <= nx <= N-1 and 0 <= ny <= M-1 and not v[nx][ny] and grid[nx][ny] == 0 :
                v[nx][ny] = 1
                q.append((nx, ny))
    return v

def count_safety(virus_region) :
    cnt = 0
    for x in range(N) :
        for y in range(M) :
            # 빈 구역이였으며 바이러스 감염되지도 않았다면
            if grid[x][y] == 0 and virus_region[x][y] == 0 :
                cnt += 1
    return cnt


# 벽 세 개 세우기
best_max = 0
for i in range(N * M - 2):
    x1, y1 = i // M, i % M
    if grid[x1][y1] == 0 : grid[x1][y1] = 1
    else : continue # 무조건 필요

    for j in range(i + 1, N * M - 1):
        x2, y2 = j // M, j % M
        if grid[x2][y2] == 0 : grid[x2][y2] = 1
        else: continue  # 무조건 필요

        for k in range(j + 1, N * M):
            x3, y3 = k // M, k % M
            if grid[x3][y3] == 0 : grid[x3][y3] = 1
            else : continue # 무조건 필요

            virus_region = bfs(viruses)

            best_max = max(count_safety(virus_region), best_max)


            grid[x3][y3] = 0 # 원상복구(벽 제거)

        grid[x2][y2] = 0 # 원상복구(벽 제거)

    grid[x1][y1] = 0 # 원상복구(벽 제거)

print(best_max)