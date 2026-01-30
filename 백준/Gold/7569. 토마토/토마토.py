from collections import deque

M, N, H = map(int, input().split())
ware = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

def bfs() :
    dq = deque()

    for z in range(H):
        for y in range(N):
            for x in range(M):
                if ware[z][y][x] == 1:
                    dq.append((z, y, x, 0))

    day = 0
    while dq:
        z, y, x, day = dq.popleft()
        for dx, dy, dz in [(1, 0, 0), (0, 1, 0), (-1, 0, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            nx, ny, nz = x + dx, y + dy, z + dz
            if nx < 0 or nx >= M or ny < 0 or ny >= N or nz < 0 or nz >= H:
                continue
            elif ware[nz][ny][nx] == 0:
                dq.append((nz, ny, nx, day+1))
                ware[nz][ny][nx] = 1
    return day

day = bfs()

found_zero = False
for height in ware:
    for row in height:
        if 0 in row:
            print(-1)
            found_zero = True
            break
    if found_zero:
        break
else:
    print(day)