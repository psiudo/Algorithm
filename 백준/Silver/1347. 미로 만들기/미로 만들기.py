cmd_len = int(input())
cmds = input()

N = 2*cmd_len + 1
grid = [['#']*N for _ in range(N)]
sx, sy, drt = N//2, N//2, 0
dv = [(1,0), (0,-1), (-1,0), (0,1)]
x, y = sx, sy
grid[x][y] = '.'
for cmd in cmds :
    if cmd == 'R' :
        drt = (drt + 1) % 4
    elif cmd == 'L' :
        drt = (drt - 1) % 4
    elif cmd == 'F' :
        x, y = x + dv[drt][0], y + dv[drt][1]
        grid[x][y] = '.'

top, left = N, N
bottom, right = 0, 0
for x in range(N) :
    for y in range(N) :
        if grid[x][y] == '.' :
            top = min(top, x)
            bottom = max(bottom, x)
            left = min(left, y)
            right = max(right, y)


for row in grid[top:bottom+1]:
    print(''.join(row[left:right+1]))