"""
x는 열의 바닥
맨해튼 거리 ; 사대의 y좌표는 0 취급
<= L 이내 사격가능
100_000개의 사대에 대해서 모든 좌표를 훑는 것은 불가능
동물들을 지워나가면서 
또는 동물 영역에 사대가 포함되느냐 논리로 간다면
여전히 100000*100000 = 100억
L (1 ≤ L ≤ 1,000,000,000)??
이것도 이분탐색 갈기자.
1) 기준점이 없다.
2) 사정거리 밖에 있다면 늘릴 것인지 줄일 것인지
"""
import bisect

M, N, L = map(int, input().split())  # 1 5 3
gun_pos = list(map(int, input().split()))
gun_pos.sort()

animals = []
for _ in range(N):
    x, y = map(int, input().split())
    animals.append((x, y))

cnt = 0
for x, y in animals:
    candi = bisect.bisect_left(gun_pos, x)
    # 가지치기
    if y > L :
        continue
    
    # 해당값이 없다면
    if M <= candi:
        candi -= 1
    # 현재 포인터와
    if abs(gun_pos[candi] - x) + y <= L:
        cnt += 1
        continue
    # 왼쪽까지
    if abs(gun_pos[candi-1] - x) + y <= L:
        cnt += 1
        continue

print(cnt)
