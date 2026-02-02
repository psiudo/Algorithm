grid = []
for _ in range(19) :
    grid.append(list(map(int, input().split())))

dv = [(0, 1), (1, 0), (1, 1), (-1, 1)] # 수평, 수직, 남동 \, 남서 /
############################### 북동으로 바꿔!!!!!!!!!!!!!#################

def is_boundary(r, c) :
    if 0 <= r <= 18 and 0 <= c <= 18 :
        return True

def check(start_color, x, y, drt):
    # 왼쪽 케이스 점검
    nx, ny = x - drt[0], y - drt[1]
    if is_boundary(nx, ny) and grid[nx][ny] == start_color :
        return False
    # 오른쪽 더 있는 거 점검
    nx, ny = x + 5*drt[0], y + 5*drt[1]
    if is_boundary(nx, ny) and grid[nx][ny] == start_color :
        return False

    # 오목인지 점검
    for k in range(1, 5) :
        nx, ny = x + k*drt[0], y + k*drt[1]
        if is_boundary(nx, ny) and grid[nx][ny] == start_color :
            continue
        else :
            return False
    return True

decide = 0 # 승부 결정 판별 플래그
ans = []
for x in range(19) :
    for y in range(19) :

        start_color = grid[x][y] # 시작 돌의 색

        # 남동 점검
        if 0 <= y <= 14 and 0 <= x <= 14 : # 14 15 16 17 18 남동
            # print('x와 y그리고 시작 색은', x, y, start_color)
            if start_color != 0 and check(start_color, x, y, dv[2]):
                ans = [(x, y, start_color)]

        # 남서 점검 XXXXXX 북동 점검
        if 0 <= y <= 14 and 4 <= x <= 18 : # 0 1 2 3 4 # 남서
            if start_color != 0 and check(start_color, x, y, dv[3]):
                ans = [(x, y, start_color)]

        # 수평 점검
        if start_color != 0 and check(start_color, x, y, dv[0])  :
            ans = [(x, y, start_color)]


        # 수직 점검
        if start_color != 0 and check(start_color, x, y, dv[1]) :
            ans = [(x, y, start_color)]



# 답 낼 때, 1인덱스로 바꾸기. 검은색 승 1 / 흰색 승 2
if len(ans) == 0 :
    print(0)
elif ans[0][2] == 1 :
    print(1)
    print(ans[0][0]+1, ans[0][1]+1)
elif ans[0][2] == 2 :
    print(2)
    print(ans[0][0]+1, ans[0][1]+1)

