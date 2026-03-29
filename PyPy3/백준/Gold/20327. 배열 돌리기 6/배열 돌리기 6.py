# ====================================================================
from itertools import product
# ====================================================================
def extract_sub(x, y, size):
    return [row[y:y + size] for row in grid[x:x + size]]
# ----------------------------------------------------------
def execute_basic_operate(mode, sub):
    if mode == 1 :
        sub = sub[::-1]
    elif mode == 2 :
        sub = [row[::-1] for row in sub]
    if mode == 3 :
        sub = [row[::-1] for row in list(map(list, zip(*sub)))]
    elif mode == 4 :
        sub = list(map(list, zip(*sub)))[::-1]
    return sub
# ----------------------------------------------------------
def paste(ltx, lty, size):
    for x in range(size) :
        for y in range(size) :
            grid[ltx+x][lty+y] = sub[x][y]
# ====================================================================
N, R = map(int, input().split())
N = 2 ** N
grid = [list(map(int, input().split())) for _ in range(N)]
for _ in range(R):
    k, l = map(int, input().split())  # k번 연산 / 단계 l
    # A) 1, 2, 3, 4번 연산
    if k in (1, 2, 3, 4) :
        for ltx, lty in product(range(0, N, 2 ** l), repeat=2):
                # 1) 부분 배열 반환
                sub = extract_sub(ltx, lty, 2 ** l)
                # 2) 연산 시행
                sub = execute_basic_operate(k, sub)
                # 3) 덮어씌우기
                paste(ltx, lty, 2**l)

    # B) 5, 6, 7, 8번 연산
    elif k in (5, 6, 7, 8) :
        # 1) 부분배열 반환 - 새로운 그리드 만들기
        new_grid = []
        for sx in range(0, N, 2 ** l) :
            temp_row = []
            for sy in range(0, N, 2 ** l) :
                # a) 부분 배열 반환
                sub = extract_sub(sx, sy, 2 ** l)
                # b) temp_row에 저장
                temp_row.append(sub)
            new_grid.append(temp_row)

        grid = new_grid # 복사 주의!

        # 2) 연산 시행
        covert_k = {5 : 1, 6 : 2, 7 : 3, 8 : 4}
        k = covert_k[k]
        grid = execute_basic_operate(k, grid)

        # 3) flatten
        new_N = N // 2**l
        new_grid = [[] for _ in range(N)]
        sx = 0
        for row in grid :
            for sub in row :
                for x in range(len(sub)) :
                    for y in range(len(sub[0])) :
                        new_grid[sx+x].append(sub[x][y])
            sx += 2**l

        grid = new_grid # 복사 주의!
# ====================================================================
for row in grid :
    print(*row)