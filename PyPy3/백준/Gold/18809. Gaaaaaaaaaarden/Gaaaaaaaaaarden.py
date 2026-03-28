# ===========================================================================================
from itertools import combinations
from collections import deque

N, M ,G, R = map(int, input().split())
original_grid = [ list(map(int, input().split())) for _ in range(N)]
dv = [(0, 1), (1, 0), (-1, 0), (0, -1)]
# ===========================================================================================
def inb(x, y) :
    return 0 <= x <= N-1 and 0 <= y <= M-1
# -----------------------------------------------------------------
def bfs(g, r) :
    g, r = [spread[i] for i in g], [spread[i] for i in r]
    Gq, Rq = deque(g), deque(r)
    # 방문처리
    v = [[0]*M for _ in range(N)]
    for x, y in  g :
        v[x][y] = 1
        grid[x][y] = 4
    for x, y in r :
        v[x][y] = 2
        grid[x][y] = 5

    while Gq or Rq :
        for _ in range(len(Gq)) :
            x, y = Gq.popleft()

            if grid[x][y] == 6 : continue
            if grid[x][y] == 3 : grid[x][y] = 4 # 초록색 배양액 확정

            for dx, dy in dv :
                nx, ny = x + dx, y + dy
                if not inb(nx, ny) : continue # 범위 내
                if v[nx][ny] : continue # 미방문
                if 1 <= grid[nx][ny] <= 2 :
                    grid[nx][ny] = 3 # 가계약 G는 3으로
                    v[nx][ny] = 1 # 가계약 v는 1로
                    Gq.append((nx, ny))

        for _ in range(len(Rq)) :
            x, y = Rq.popleft()
            
            if grid[x][y] == 6 : continue

            for dx, dy in dv :
                nx, ny = x + dx, y + dy
                if not inb(nx, ny) : continue # 범위 내
                if v[nx][ny] >= 2 : continue # 가계약 v까지 허용
                if 1 <= grid[nx][ny] <= 3 :

                    if grid[nx][ny] == 3 : grid[nx][ny] = 6 # 동시에 배양액을 뿌렸다면
                    else : grid[nx][ny] = 5

                    v[nx][ny] = 2 # 여기서 확정
                    Rq.append((nx, ny))

    flower = 0
    for x in range(N) :
        for y in range(M) :
            if grid[x][y] == 6:
                flower += 1
    return flower
# ===========================================================================================
# [1] : 배양액 땅을 모은다. # 0 : 호수 / 1 : 배양액 x / 2 : 배양액 o
spread = [(x, y) for x in range(N) for y in range(M) if original_grid[x][y] == 2]
# [2] : 그 중에서 G를 고르고 R을 고르는 작업을 반복하여 각각의 경우에 대해 BFS의 결과를 얻는다.
ans = 0
idx_set = set(range(len(spread)))
for g in combinations(idx_set, G) :
    for r in combinations(idx_set - set(g), R) :
        # [2] - A : BFS를 돌려 결과를 얻는다.
        grid = [row[:] for row in original_grid]
        f = bfs(g, r)
        ans = max(ans, f)
# ===========================================================================================
print(ans)