# ===========================================================================================
from itertools import combinations
from collections import deque

# ===========================================================================================
LAKE = 0  # 호수
NO_CULTURE = 1  # 배양액을 뿌릴 수 없는 땅
CULTURE_POSSIBLE = 2  # 배양액을 뿌릴 수 있는 땅
GREEN_TEMP = 3  # 초록색 배양액 가계약 (이번 턴에 도착함)
GREEN_DONE = 4  # 초록색 배양액 확정 (완전히 퍼짐)
RED_DONE = 5  # 빨간색 배양액 확정 (완전히 퍼짐)
FLOWER = 6  # 꽃이 피어남
# ===========================================================================================
N, M, G, R = map(int, input().split())
original_grid = [list(map(int, input().split())) for _ in range(N)]
dv = [(0, 1), (1, 0), (-1, 0), (0, -1)]
# ===========================================================================================
def inb(x, y):
    return 0 <= x <= N - 1 and 0 <= y <= M - 1
# ---------------------------------------------------------
def bfs(g_idx, r_idx):
    g = [spread[i] for i in g_idx]
    r = [spread[i] for i in r_idx]

    Gq, Rq = deque(g), deque(r)
    v = [[0] * M for _ in range(N)]

    for x, y in g:
        v[x][y] = 1
        grid[x][y] = GREEN_DONE
    for x, y in r:
        v[x][y] = 2
        grid[x][y] = RED_DONE

    while Gq or Rq:
        for _ in range(len(Gq)):
            x, y = Gq.popleft()

            if grid[x][y] == FLOWER: continue
            if grid[x][y] == GREEN_TEMP: grid[x][y] = GREEN_DONE

            for dx, dy in dv:
                nx, ny = x + dx, y + dy
                if not inb(nx, ny): continue
                if v[nx][ny]: continue

                if grid[nx][ny] in (NO_CULTURE, CULTURE_POSSIBLE):
                    grid[nx][ny] = GREEN_TEMP
                    v[nx][ny] = 1
                    Gq.append((nx, ny))

        for _ in range(len(Rq)):
            x, y = Rq.popleft()

            if grid[x][y] == FLOWER: continue

            for dx, dy in dv:
                nx, ny = x + dx, y + dy
                if not inb(nx, ny): continue
                if v[nx][ny] >= 2: continue

                if grid[nx][ny] in (NO_CULTURE, CULTURE_POSSIBLE, GREEN_TEMP):

                    if grid[nx][ny] == GREEN_TEMP: grid[nx][ny] = FLOWER
                    else: grid[nx][ny] = RED_DONE

                    v[nx][ny] = 2
                    Rq.append((nx, ny))

    flower = 0
    for x in range(N):
        for y in range(M):
            if grid[x][y] == FLOWER:
                flower += 1
    return flower
# ===========================================================================================
spread = [(x, y) for x in range(N) for y in range(M) if original_grid[x][y] == CULTURE_POSSIBLE]

ans = 0
idx_set = set(range(len(spread)))
for g_idx in combinations(idx_set, G):
    for r_idx in combinations(idx_set - set(g_idx), R):
        grid = [row[:] for row in original_grid]
        f = bfs(g_idx, r_idx)
        ans = max(ans, f)
# ===========================================================================================
print(ans)