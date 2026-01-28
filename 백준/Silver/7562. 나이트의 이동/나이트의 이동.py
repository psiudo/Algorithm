T = int(input())
for _ in range(T):
    l = int(input())
    sx, sy = map(int, input().split())
    gx, gy = map(int, input().split())

    # 나이트의 8가지 이동 방향
    dv = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
    q = [(sx, sy)]
    v = [[0] * l for _ in range(l)]
    v[sx][sy] = 1
    dist = [[0] * l for _ in range(l)]

    while q :
        x, y = q.pop(0)

        for dx, dy in dv:
            nx, ny = x + dx, y + dy

            # 범위 및 방문 조건 체크
            if 0 <= nx <= l-1 and 0 <= ny <= l-1 and not v[nx][ny]:
                v[nx][ny] = 1
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
                # 여기서 종료조건가능
                if (nx, ny) == (gx, gy):
                    break
    print(dist[gx][gy])
