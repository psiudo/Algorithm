from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
######################################################
visited = [0] * (N * M)
queue = deque([(0, 0, 1)])  # x, y, 현재 이동 거리
visited[0] = 1  # 시작점 방문 처리

while queue:
    x, y, dist = queue.popleft()

    if (x, y) == (N - 1, M - 1):
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            idx = nx * M + ny
            if maze[nx][ny] == 1 and not visited[idx]:  # 이동 가능 & 방문 안 했으면
                visited[idx] = 1
                queue.append((nx, ny, dist + 1))
######################################################
print(dist)
