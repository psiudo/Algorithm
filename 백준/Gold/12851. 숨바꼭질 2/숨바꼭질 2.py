"""
읽기+구상 : 1:00 / 코드 : 5:00 / 디버깅 : 30:00 / 실패횟수 : 5++ / 제출횟수 : 1
"""

"""
최우선 순위는 걸린 시간 그리고 그 다음은 목적지와의 거리?
"""

import heapq

N, K = map(int, input().split()) # 0 ~ 100_000

upper = 2 * max(N, K)

# 전역 V를 사용하면 다른 브랜치에서 방문이 허용되야 할 때 망한다.
hq = [(0, N)] # t와 초기 위치
heapq.heapify(hq)

cnt = 0 # 경우의 수

v = [100_000] * upper # 두배까지만
v[N] = 0
while hq :
    t, pos = heapq.heappop(hq)

    if pos == K :
        if t <= v[pos] :
            cnt += 1
        continue
    for nxt in (2*pos, pos-1, pos+1) :
        if 0 <= nxt <= upper - 1 and t + 1 <= v[nxt] : # 경로 수니까 등식 포함
            v[nxt] = t+1
            heapq.heappush(hq, (t+1, nxt))


print(v[K])
print(cnt)