# ==============================================
# Normarlize
# ==============================================
# 빙고판
grid = []
for _ in range(5) :
    grid.append(list(map(int, input().split())))

# 부르는 숫자
call_nums = []
for _ in range(5) :
    temp = map(int, input().split())
    call_nums.extend(temp)

# 똑같은 크기의 방문 배열
v = [[0]*5 for _ in range(5)]

# ================================================
# ==============================================
# Identify
# 한 수를 둘 때마다, 그 수의 4방위를 확인한다.
# 새로운 빙고배열이 추가되면 tot에 더한다.
# ==============================================
dv = [(1,1), (1,-1)]
def check(x, y) :
    cnt = 0
    # 수평 확인
    for move in range(5) :
        if v[x][move] == 1 :
            continue
        else :
            break
    else :
        cnt += 1

    # 수직 확인
    for move in range(5) :
        if v[move][y] == 1 :
            continue
        else :
            break
    else :
        cnt += 1

    # 대각1 확인
    if x - y == 0 : # 대각 오른쪽 아래라면
        nx, ny = 0, 0
        for _ in range(5) :
            if v[nx][ny] == 0 :
                break
            nx, ny = nx + 1, ny + 1
        else :
            cnt += 1

    # 대각2 확인
    if x + y == 4 : # 대각 왼쪽 아래라면
        nx, ny = 0, 4
        for _ in range(5) :
            if v[nx][ny] == 0 :
                break
            nx, ny = nx + 1, ny - 1
        else :
            cnt += 1

    return cnt
# ==============================================
# Apply
# 빙고판을 확인하면서 숫자 방문하고 check함수를 호출해 식별한다.
# ==============================================

tot = 0
found = False
for idx, num in enumerate(call_nums) :
    if found : break
    for x in range(5) :
        if found: break
        for y in range(5) :
            if found: break
            if grid[x][y] == num :
                v[x][y] = 1 # 방문처리하고
                tot += check(x, y)

                if tot >= 3 :
                    result = idx + 1
                    found = True
                    break

# ==============================================
# Report
# ==============================================
print(result)
