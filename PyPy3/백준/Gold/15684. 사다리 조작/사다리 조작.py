n, m, h = map(int, input().split())
grid = [ [-1]*n for _ in range(h) ]
for _ in range(m) :
    a, b = map(lambda p : int(p)-1, input().split())
    grid[a][b] = b + 1
    grid[a][b+1] = b
# ==============================================================
def p_grid(name ,arr) :
    print(f"{'='*10} {name} {'='*10}")
    for row in arr :
        for cell in row :
            if cell == -1 : cell = "."
            print(f"{cell:>3}", end="")
        print()
# -------------------------------------------------
def check_success() :
    for y in range(n) :
        ty = y
        for x in range(h) :
            if grid[x][y] != -1 :
                y = grid[x][y]
        if ty != y :
            return False
    return True
# ==============================================================
def dfs(depth, sh, sn) :
    global min_line

    if depth >= min_line :
        return

    if check_success() :
        min_line = min(min_line, depth)
        return

    if depth >= 3 :
        return

    if sn >= n-1 : # 오른쪽 끝 선이라면
        sh, sn = sh + 1, 0
    if sh == h : # 아래쪽 끝 선이라면
        return

    for x in range(sh, h):
        start_y = sn if x == sh else 0
        for y in range(start_y, n - 1):
            if grid[x][y] == -1 and grid[x][y + 1] == -1:
                grid[x][y], grid[x][y + 1] = y + 1, y
                dfs(depth + 1, x, y + 2)
                grid[x][y], grid[x][y + 1] = -1, -1

# ==============================================================
min_line = 4
# p_grid("초기 그리드", grid)
if check_success() : print(0)
else :
    dfs(0, 0, 0)
    if min_line == 4 : print(-1)
    else : print(min_line)