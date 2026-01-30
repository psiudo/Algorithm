from collections import deque
import sys

input = sys.stdin.readline

# 입력 받기: M은 가로, N은 세로 크기
M, N = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

queue = deque()
# 날짜 정보를 기록할 격자 (초기 값은 0)
days = [[0] * M for _ in range(N)]

# 초기 익은 토마토 위치 추가
for i in range(N):
    for j in range(M):
        if grid[i][j] == 1:
            queue.append((i, j))

# 상하좌우 방향 정의
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while queue:
    x, y = queue.popleft()
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if grid[nx][ny] == 0:
                grid[nx][ny] = 1  # 토마토를 익힌다.
                days[nx][ny] = days[x][y] + 1
                queue.append((nx, ny))

result = 0
for i in range(N):
    for j in range(M):
        # 익지 않은 토마토가 있다면 -1 출력
        if grid[i][j] == 0:
            print(-1)
            exit(0)
        result = max(result, days[i][j])

print(result)
