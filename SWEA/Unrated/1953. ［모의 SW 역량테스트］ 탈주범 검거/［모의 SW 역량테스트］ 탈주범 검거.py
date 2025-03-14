from collections import deque

# 방향 벡터 정의: 0=상, 1=우, 2=하, 3=좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

PIPE = {
    0: [0, 0, 0, 0],
    1: [1, 1, 1, 1],    # 상하좌우
    2: [1, 0, 1, 0],    # 상하
    3: [0, 1, 0, 1],    # 좌우
    4: [1, 1, 0, 0],    # 상우
    5: [0, 1, 1, 0],    # 우하
    6: [0, 0, 1, 1],    # 하좌
    7: [1, 0, 0, 1],    # 좌상
}

def bfs_boolean(N, M, R, C, L, tunnel):

    visited = [[False]*M for _ in range(N)]
    visited[R][C] = True

    queue = deque()
    queue.append((R, C, 1))
    count = 1

    while queue:
        r, c, t = queue.popleft()

        if t == L:
            continue

        cur_pipe = tunnel[r][c]
        cur_dirs = PIPE[cur_pipe]

        # 4방향 탐색
        for i in range(4):
            if cur_dirs[i] == 0:
                continue

            nr, nc = r + dy[i], c + dx[i]

            if not (0 <= nr < N and 0 <= nc < M):
                continue

            if tunnel[nr][nc] == 0:
                continue

            nxt_pipe = tunnel[nr][nc]
            nxt_dirs = PIPE[nxt_pipe]
            opp = (i + 2) % 4
            if nxt_dirs[opp] == 0:
                continue

            if not visited[nr][nc]:
                visited[nr][nc] = True
                count += 1
                queue.append((nr, nc, t + 1))

    return count

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]

    answer = bfs_boolean(N, M, R, C, L, tunnel)
    print(f"#{tc} {answer}")

