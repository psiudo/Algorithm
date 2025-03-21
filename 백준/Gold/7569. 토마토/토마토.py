import sys

input = sys.stdin.readline
from collections import deque

M, N, H = map(int, input().split())
ware = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

dq = deque()

for z in range(H):
    for y in range(N):
        for x in range(M):
            if ware[z][y][x] == 1:
                dq.append((z, y, x))

day = 0
while dq:
    for _ in range(len(dq)):
        z, y, x = dq.popleft()
        for dx, dy, dz in [(1, 0, 0), (0, 1, 0), (-1, 0, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            nx, ny, nz = x + dx, y + dy, z + dz
            if 0 <= nx < M and 0 <= ny < N and 0<= nz < H and ware[nz][ny][nx] == 0:
                dq.append((nz, ny, nx))
                ware[nz][ny][nx] = 1
    day += 1

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
    print(day - 1)
