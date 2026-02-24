R, C, T = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(R)]

it = ((x, y) for x in range(R) for y in range(C) if grid[x][y] == -1)
up_x, up_y = next(it)
down_x, down_y = next(it)


def diffuse_dust():
    temp_grid = [[0] * C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if grid[x][y] >= 1:
                give = grid[x][y] // 5
                for dx, dy in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx <= R - 1 and 0 <= ny <= C - 1 and grid[nx][ny] != -1:  # 공기청정기가 아니라면
                        temp_grid[nx][ny] += give  # 해당 방향으로 확산
                        temp_grid[x][y] -= give  # 본인 위치 감소

    return temp_grid


def operate_purifier():
    x, y = down_x + 1, down_y  # down훼손 금지

    while True:
        if (x, y) == (down_x + 1, 0):
            grid[x][y] = 0
            x += 1
            continue

        # y == 0 -> x == R-1 -> y == C-1 -> x == down_x
        if y == 0:
            if x != R:
                grid[x - 1][y] = grid[x][y]  # 위로 옮기기
                x += 1
            else:
                x, y = R - 1, 1  # 오른칸으로 전환

        elif x == R - 1:
            if y != C:
                grid[x][y - 1] = grid[x][y]  # 왼쪽으로 옮기기
                y += 1
            else:
                x, y = R - 2, C - 1  # 위쪽 칸으로 전환

        elif y == C - 1:
            if x != down_x - 1:
                grid[x + 1][y] = grid[x][y]  # 아래 칸으로 옮기기
                x -= 1
            else:
                x, y = down_x, C - 2  # 왼쪽 칸으로 전환

        elif x == down_x:
            if y != 1:
                grid[x][y + 1] = grid[x][y]  # 오른쪽으로 옮기기
                y -= 1
            else:
                break  # 중지

    # 마지막 수동으로
    grid[x][y + 1] = grid[x][y]
    grid[x][y] = 0

    # ===================================================
    x, y = up_x - 1, up_y  # down훼손 금지

    while True:
        if (x, y) == (up_x - 1, 0):
            grid[x][y] = 0
            x -= 1
            continue

        # y == 0 -> x == R-1 -> y == C-1 -> x == down_x
        if y == 0:
            if x != -1:
                grid[x + 1][y] = grid[x][y]  # 아래로 옮기기
                x -= 1
            else:
                x, y = 0, 1  # 오른칸으로 전환

        elif x == 0:
            if y != C:
                grid[x][y - 1] = grid[x][y]  # 왼쪽으로 옮기기
                y += 1
            else:
                x, y = 1, C - 1  # 위쪽 칸으로 전환

        elif y == C - 1:
            if x != up_x + 1:
                grid[x - 1][y] = grid[x][y]  # 위쪽 칸으로 옮기기
                x += 1
            else:
                x, y = up_x, C - 2  # 왼쪽 칸으로 전환

        elif x == up_x:
            if y != 1:
                grid[x][y + 1] = grid[x][y]  # 오른쪽으로 옮기기
                y -= 1
            else:
                break  # 중지

    # 마지막 수동으로
    grid[x][y + 1] = grid[x][y]
    grid[x][y] = 0


# ==========================================================================

for _ in range(T):
    delta_grid = diffuse_dust()
    for x in range(R):
        for y in range(C):
            if grid[x][y] != -1:  # 공기청정기가 아니라면
                grid[x][y] += delta_grid[x][y]
    operate_purifier()


ans = sum(grid[x][y] for x in range(R) for y in range(C)) + 2
print(ans)
