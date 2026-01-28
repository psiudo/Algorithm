T = int(input())
for _ in range(T):
    l = int(input())
    sx, sy = map(int, input().split())
    gx, gy = map(int, input().split())

    # 나이트의 8가지 이동 방향
    dv = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
    q = [(sx, sy)]
    dist = [[0] * l for _ in range(l)]

    while q :
        x, y = q.pop(0)

        # 여기에서 종료조건해야 한번 다른 데 가다가 돌아오는 경우 없다.
        if (x, y) == (gx, gy):
            break

        for dx, dy in dv:
            nx, ny = x + dx, y + dy

            # 범위 및 방문 조건 체크
            if 0 <= nx <= l-1 and 0 <= ny <= l-1 and not dist[nx][ny]:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

    print(dist[gx][gy])
