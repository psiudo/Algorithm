# ==============================================
# Normalize
# ==============================================
N, K = map(int, input().split())
lst = [] # 집들의 위치
for _ in range(N) :
    lst.append(list(map(int, input().split())))
# print(lst) [[0, 0], [0, 5], [5, 0], [5, 5]]
# =================================================
# Identify & Apply
# Max min 문제이면서 조합 문제지만 K >= 3이라면 중복순열로
# =================================================


# 1) 일단 대피소 중에서 가장 짧은 거리 찾기
# 2) 대피소와 집의 거리들 중에서 가장 먼거리 찾기
#############################################################
def calculate(choice) : # 현재 선택 중에서 최대 거리 찾기

    dist_list = []
    for x, y in lst : # x, y : 평범한 집 중에서
        temp_list = []
        for cx, cy in choice : # cx, cy : 대피소 중에서
            if [x, y] in choice:
                # 평범한 집이 아니라 대피소 중에서 한 곳이었다면 이번 x, y는 건너뛰기.
                continue

            # 현재 집(x, y) ~ 대피소 (cx, cy)들 간의 거리 모으기
            temp_list.append(abs(cx - x) + abs(cy - y))

        # 대피소가 아닌 집은 temp_list에 모였으니까 그 중에서 짧은 거리 넣기
        # 즉 모든 집에 대한 대피소까지 거리 모였다.
        if temp_list :
            dist_list.append(min(temp_list))

    if dist_list :
        return max(dist_list)
    else :
        return 0

#############################################################
best = float('inf')
def dfs(depth, cnt, choice) : # 몇 단계, 선택 갯수
    # print(choice) [[0, 0], [0, 5]]
    global best

    # 거리 갱신 먼저
    if cnt == K :
        curr_max = calculate(choice)
        if best > curr_max : # 최선보다 작으면
            best = curr_max
        return # 어쨌든 리턴

    # 종료 조건
    if depth == N : # N일 때, 직전 N-1번에서 N개까지 선택완료
        return # 여기도 리턴

    dfs(depth+1, cnt, choice)
    dfs(depth+1, cnt+1, choice + [ lst[depth] ] ) # depth번째 집을 선택

# ==============================================
# Report
# ==============================================
dfs(0, 0, [])
print(best)