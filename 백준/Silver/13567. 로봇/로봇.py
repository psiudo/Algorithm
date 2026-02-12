###########  M + 1개 의 격자 #########
"""
TURN0 : 왼쪽으로 90도
TURN1 : 오른쪽으로 90도
MOVEd : d만큼 이동

유효하지 않은 명령어 열이라면 -1 출력
처음 시작 : (M-1, 0) 그리고 R 향하는 중 
"""
M, n = map(int, input().split())
grid = [[0] * (M+1) for _ in range(M+1)]

dv = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # R D L U

def inb(x, y):
    if 0 <= x <= M and 0 <= y <= M: return True
    return False


def move(d, x, y, drt):
    global valid

    dx, dy = dv[drt]
    nx, ny = x + d*dx, y + d*dy # d만큼 곱해야 한다.
    if inb(nx, ny) : return nx, ny, drt
    else :
        valid = False
        return x, y, drt

def turn(mode, x, y, drt):
    if mode == 0: # 왼쪽으로 = 반시계
        return x, y, (drt - 1) % 4 
    elif mode == 1: # 오른쪽으로 = 시계
        return x, y, (drt + 1) % 4


sx, sy = M, 0  # 초기 시작 위치
x, y, drt = sx, sy, 0  # 처음 출발 위치 + 오른쪽 방향
valid = True  # 명령어 유효성 검증

for _ in range(n):
    cmd, d = map(str, input().split())
    if cmd == "MOVE":
        x, y, drt = move(int(d), x, y, drt)  # 반환 값은 항상 새로운 위치 + 방향
        if not valid:
            break

    elif cmd == "TURN":
        mode = int(d)
        x, y, drt = turn(mode, x, y, drt)  # 반환 값은 항상 새로운 위치 + 방향
        if not valid:
            break


if not valid:
    print(-1)
elif valid:
    print(y, M-x)
