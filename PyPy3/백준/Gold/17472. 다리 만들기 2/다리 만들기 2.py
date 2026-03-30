from collections import deque

d_to_chr = {0: '-', 1: '|', 2: '|', 3: '-'}
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]
# ===========================================================================
def inb(p, q):
    return 0 <= p <= N - 1 and 0 <= q <= M - 1

def collect_node(x, y):
    q = deque([(x, y)])
    v[x][y] = 1
    node = [(x, y)]
    while q:
        x, y, = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not inb(nx, ny): continue
            if grid[nx][ny] == 0: continue
            if v[nx][ny]: continue
            q.append((nx, ny))
            v[nx][ny] = 1
            node.append((nx, ny))
    return node

def connect_bridge(x, y, d, node):
    node_set = set(node)
    length = 0
    path = []
    while True:
        nx, ny = x + dx[d], y + dy[d]
        if not inb(nx, ny): return False, []
        if (nx, ny) in node_set: return False, []
        if grid[nx][ny] == 1 and length == 1: return False, []
        if grid[nx][ny] == 1 and length >= 2: break

        path.append((nx, ny))
        length += 1
        x, y = nx, ny

    bridge = d_to_chr[d]
    for x, y in path:
        if grid[x][y]:
            grid[x][y] = str(grid[x][y]) + bridge
        else:
            grid[x][y] = bridge
    return length, path

def revert_bridge(path):
    for x, y in path:
        if len(str(grid[x][y])) == 1:
            grid[x][y] = 0
        else:
            grid[x][y] = str(grid[x][y])[:-1]

opp = [3, 2, 1, 0]
def can_go(cell, d):
    if cell == 0: return False
    if type(cell) == int: return True
    return ('-' in cell and d in (0, 3)) or ('|' in cell and d in (1, 2))

def check_connect():
    start_x, start_y = Node[0][0]
    # 큐 상태: (x, y, b_dir) -> b_dir: -1(섬), 0(가로다리), 1(세로다리)
    q = deque([(start_x, start_y, -1)])
    check_v = {(start_x, start_y, -1)}

    while q:
        x, y, b_dir = q.popleft()

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if not inb(nx, ny): continue

            if b_dir == 0 and d not in (0, 3): continue
            if b_dir == 1 and d not in (1, 2): continue

            if not can_go(grid[x][y], d): continue
            if not can_go(grid[nx][ny], opp[d]): continue

            nxt_val = grid[nx][ny]
            nxt_b_dir = -1
            if type(nxt_val) == str:
                if d in (0, 3):
                    nxt_b_dir = 0
                else:
                    nxt_b_dir = 1

            if (nx, ny, nxt_b_dir) in check_v: continue

            check_v.add((nx, ny, nxt_b_dir))
            q.append((nx, ny, nxt_b_dir))

    visited_islands = set((r, c) for r, c, b_type in check_v if b_type == -1)
    for node in Node:
        if set(node) - visited_islands:
            return False
    return True
# ===========================================================================
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

v = [[0] * M for _ in range(N)]
Node = []
for x in range(N):
    for y in range(M):
        if grid[x][y] == 0: continue
        if v[x][y]: continue
        node = collect_node(x, y)
        Node.append(node)
# ===========================================================================
all_bridges = []
seen_path = set()

for i in range(len(Node)):
    for x, y in Node[i]:
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if not inb(nx, ny): continue
            if grid[nx][ny] != 0: continue

            length, path = connect_bridge(x, y, d, Node[i])
            if not length: continue

            revert_bridge(path)

            key = tuple(sorted(path))
            if key in seen_path: continue
            seen_path.add(key)

            all_bridges.append((path, d_to_chr[d], length))

all_bridges.sort(key=lambda x: x[2])
# ===========================================================================
need = len(Node) - 1
def dfs(depth, picked, curr_length):
    global ans

    if curr_length >= ans: return

    if picked == need:
        if check_connect():
            ans = min(ans, curr_length)
        return

    if depth == len(all_bridges): return

    path, bridge_char, length = all_bridges[depth]

    for x, y in path:
        if grid[x][y]:
            grid[x][y] = str(grid[x][y]) + bridge_char
        else:
            grid[x][y] = bridge_char

    dfs(depth + 1, picked + 1, curr_length + length)
    revert_bridge(path)
    dfs(depth + 1, picked, curr_length)
# ===========================================================================
ans = 10 ** 6
dfs(0, 0, 0)
print(-1 if ans == 10 ** 6 else ans)