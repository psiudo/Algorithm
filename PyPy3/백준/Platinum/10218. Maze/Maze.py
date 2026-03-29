TC = int(input())
for CN in range(1, TC+1) :
    N, M = map(int, input().split())
    grid = [list(input()) for _ in range(N)]
    all_pos = set([(x, y) for x in range(N) for y in range(M) if grid[x][y] == '.'])
    dx = [0, -1, 0, 1] # L / U / R / D
    dy = [-1, 0, 1, 0]
    d_to_drt = {0 : 'L', 1 : 'U', 2 : 'R', 3 : 'D'}
    # ============================================================================================
    def push(d, curr_set) :
        next_set = set()
        for x, y in curr_set :
            escape = False
            while True :
                nx, ny = x + dx[d], y + dy[d]
                if grid[nx][ny] == 'O' : escape = True; break
                elif grid[nx][ny] == "#" : break
                x, y = nx, ny
            if not escape : next_set.add((x, y))
        return next_set
    # ----------------------------------------------------------------------------
    def dfs(depth, path, curr_set) :
        if not curr_set :
            return path

        if depth >= 10 :
            return

        for d in (0, 1, 2, 3) :
            if path and path[-1] == d : continue
            next_set = push(d, curr_set)
            res = dfs(depth + 1, path + [d], next_set)
            if res : return res
    # ============================================================================================
    path = dfs(0, [], all_pos)
    if path :
        ans = ""
        for d in path :
            ans += d_to_drt[d]
    else :
        ans = "XHAE"
    print(ans)