"""
행은 위에서부터 1번
열은 왼쪽에서부터 1번 
십자가의 개수는 N×M이하

BFS랑 퍼지는 모양이 똑같다.
"""

N, M = map(int, input().split())
grid = [list(input()) for _ in range(N)]

dv = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def inb(x, y):
    if 0 <= x <= N - 1 and 0 <= y <= M - 1: return True
    return False


def apply(x, y):
    flag = False
    for k in range(1, max(N, M) + 1) :
        if flag : break
        for i in range(4):
            dx, dy = dv[i]
            nx, ny = x + k * dx, y + k * dy
            if not inb(nx, ny) or grid[nx][ny] != '*' :
                flag = True
                break

    if k <= 2 : return x, y, 0
    # k가 2이하라면 k가 2또는 1루프에서 중단
    # k = 2를 넘어가지 않았다면 십자가가 아니라 점
    else : return x, y, k - 2 # 다음 k루프에서 break 됐기 때문에 -1 그리고 십자가 크기 보정 -1

def paint(x, y, size) :
    for k in range(size+1) : # 십자가 사이즈 1이라면 2개를 그려야 한다.
        for i in range(4):
            dx, dy = dv[i]
            nx, ny = x + k * dx, y + k * dy
            new_grid[nx][ny] = '*'

new_grid = [['.']*M for _ in range(N)]
ans = []
for x in range(N):
    for y in range(M):
        if grid[x][y] == '*' :
            x, y, size = apply(x, y)
            if size >= 1 :
                paint(x, y, size) # new_grid에 그리기
                ans.append([x+1, y+1, size]) # 1 인덱스로 저장

# ===================================================================
if all(grid[x][y] == new_grid[x][y] for x in range(N) for y in range(M)) :
    print(len(ans))
    for a in ans :
        print(*a)
else :
    print(-1)
