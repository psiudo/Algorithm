N, M = map(int, input().split()) # N, M
grid = [ list(map(int, input().split())) for _ in range(N)] # Ground그리드, NxN 격자
cmds = [ tuple(map(int, input().split())) for _ in range(M) ] # d, s
# L / LR / U / UR / R / RD / D / DL
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
# 구름의 위치 저장
clouds = set()
# 0) 초기 비바라기 생성
def init_rain_magic() :
    clouds.add((N-2, 0))
    clouds.add((N-2, 1))
    clouds.add((N-1, 0))
    clouds.add((N-1, 1))

# 1) 구름 움직임
def move_clouds(drt, s) :
    temp_lst = []
    drt -= 1 # 0-인덱스로 변경
    for x, y in clouds :
        nx, ny = x + s*dx[drt], y + s*dy[drt]
        nx %= N
        ny %= N
        temp_lst.append((nx, ny))  # temp에 저장

    return temp_lst

# 2) 비 내림
def rain() :
    for x, y in clouds :
        grid[x][y] += 1


# 3) 비내림 후 구름 삭제
def delete_clouds() :
    curr_deleted = []
    for x, y in clouds :
        curr_deleted.append((x, y))

    return curr_deleted

# 4) 물복사 버그
def copy_water(prev_deleted) :
    for x, y in prev_deleted :
        cnt = 0 # 새로운 좌표마다 cnt 초기화
        for dx, dy in [(-1,-1),(-1,1), (1,-1), (1,1)] :
            nx, ny = x + dx, y + dy
            if 0 <= nx <= N-1 and 0 <= ny <= N-1 and grid[nx][ny] >= 1:

                cnt += 1
        grid[x][y] += cnt

# 5) 구름 생성 => 물의 양 2감소 ### 3)에서 삭제된 칸이 아니어야 한다.
def update_clouds(prev_deleted) :
    prev_deleted = set(prev_deleted)
    for x in range(N) :
        for y in range(N) :
            if (x, y) not in prev_deleted and grid[x][y] >= 2:
                grid[x][y] -= 2
                clouds.add((x, y))

# 0) 초기 비바라기 생성
init_rain_magic() # set자료구조 직접 수정
for drt, s in cmds :
    # 1) 구름 이동
    cloud_lst = move_clouds(drt, s)
    clouds = set(cloud_lst) # 새로운 clouds 집합

    # 2) 비 내림
    rain()
    # 3) 구름 사라짐 => 사라진 구름의 위치 반환
    prev_deleted = delete_clouds()
    clouds = set() # 빈 구름 집합

    # 4) 물복사 버그
    copy_water(prev_deleted)

    # 5) 구름 업데이트
    update_clouds(prev_deleted) # 구름 집합에 구름 생성 완료

# ==================================== 출력
ans = sum(grid[x][y] for x in range(N) for y in range(N))
print(ans)