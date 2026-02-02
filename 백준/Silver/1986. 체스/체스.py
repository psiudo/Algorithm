n, m = map(int, input().split())
a = list(map(int, input().split())) # 퀸
b = list(map(int, input().split())) # 나이트
c = list(map(int, input().split())) # 폰

queen = []
for i in range(1, 2*a[0], 2) :
    queen.append(a[i:i+2])
knight = []
for i in range(1, 2*b[0], 2) :
    knight.append(b[i:i+2])
pawn = []
for i in range(1, 2*c[0], 2) :
    pawn.append(c[i:i+2])

grid = [[0]*m for _ in range(n)]

#############################################
# 모든 격자 탐색
# pawn, knight, queen 순으로 말 놓기
# 퀸 같은 경우에는 방문 배열과 그리드 둘 다를 보고 판단한다.
for x, y in pawn :
    grid[x-1][y-1] = 1
for x, y in knight :
    grid[x-1][y-1] = 1
for x, y in queen :
    grid[x-1][y-1] = 1

#############################################
v = [[0]*m for _ in range(n)]
##########
dv = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]
for x, y in knight :
    for dx, dy in dv :
        nx, ny = x - 1 + dx, y - 1 + dy
        if 0 <= nx <= n - 1 and 0 <= ny <= m - 1 : # 있든 없든 마킹 가능
            v[nx][ny] = 1

dv = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
for x, y in queen :
    for dx, dy in dv :
        # 한 방향 탐색
        nx, ny = x - 1 + dx, y - 1 + dy
        while 0 <= nx <= n - 1 and 0 <= ny <= m - 1 and grid[nx][ny] == 0 :
            v[nx][ny] = 1 # 방문할 수 있음만 마킹
            nx += dx
            ny += dy

##############################################
cnt = 0
for x in range(n) :
    for y in range(m) :
        if grid[x][y] == 0 and v[x][y] == 0 :
            cnt += 1

print(cnt)