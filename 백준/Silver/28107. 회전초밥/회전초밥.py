from collections import deque

N, M = map(int, input().split())
people = []
for _ in range(N) :
    k, *temp = map(int, input().split())
    people.append(temp)

# 만드는 순서
orders = list(map(int, input().split()))
sushi_wants = [ deque([]) for _ in range(200_001) ] # popleft를 위함!!
for idx, person in enumerate(people) :
    for sushi in person :
        sushi_wants[sushi].append(idx) # 특정 스시 종류에 본인 번호를 넣는다.

ans = [0]*(N)
for order in orders :
    if sushi_wants[order] :
        idx = sushi_wants[order].popleft()
        ans[idx] += 1

print(*ans)