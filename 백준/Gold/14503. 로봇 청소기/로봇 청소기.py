# 3 <= N, M <= 50
N, M = map(int, input().split())
# print(N, M) # 3 3
sx, sy, sdrt = map(int, input().split()) # drt = 0 : U / 1 : R / 2 : D / 3 : L
# print(sx, sy, drt) # 1 1 0
# 방의 가장 북쪽, 남쪽, 서쪽, 동쪽 줄 중 하나 이상에 위치한 모든 칸에는 벽이 있다.
grid = [ list(map(int, input().split())) for _ in range(N) ]
dv = [(-1, 0), (0, 1), (1, 0), (0, -1)] # U R D L / 북, 동, 남, 서

def inb(nx, ny):
    if 0 <= nx <= N - 1 and 0 <= ny <= M - 1: return True
    return False

def has_uncleaned(x, y):
    for dx, dy in dv:
        nx, ny = x + dx, y + dy
        if inb(nx, ny):
            if grid[nx][ny] == 0 and not v[nx][ny]: # 빈칸 + 청소되지 않은
                return True
    return False


def rotate_move(x, y, drt):
    tx, ty, tdrt = x, y, drt
    for _ in range(4): # 마지막 네번째에 다시 자기 자신으로 돌아온다.
        ################################################################################
        drt = (drt - 1) % 4 # 다음 방향으로 바꾸기 #################먼저 바꾸기##################
        ################################################################################
        nx, ny = x + dv[drt][0], y + dv[drt][1]
        if inb(nx, ny) :
            if grid[nx][ny] == 0 and not v[nx][ny] :
                return nx, ny, drt # 좌표는 원래 좌표 drt는 회전된 방향

    else :
        # 반환하지 않고 4번의 루프를 돌았다면 원상복구
        return tx, ty, tdrt # 좌표는 원래 좌표


def able_backward(x, y, drt):
    nx, ny = x - dv[drt][0], y - dv[drt][1]
    if inb(nx, ny) and grid[nx][ny] == 0 : # 벽이 아니라면 후진 가능
        return True # 가능하므로
    else :
        return False # 불가하다면


cnt = 0
v = [ [0]*M for _ in range(N) ]

x, y, drt = sx, sy, sdrt
while True :
    # 1) 청소
    if grid[x][y] == 0 and not v[x][y] :
        v[x][y] = 1
        cnt += 1

    # 2) 주변 확인 및 이동
    if has_uncleaned(x, y) :
        x, y, drt = rotate_move(x, y, drt)
    else :
        if able_backward(x, y, drt) :
            x, y, drt = x - dv[drt][0], y - dv[drt][1], drt
        # 움직임이 불가하다면
        else :
            break

print(cnt)