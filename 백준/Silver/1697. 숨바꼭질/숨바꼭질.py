from collections import deque

N, K = map(int, input().split())
q = deque([(N, 0)])
v = {}
while q :
    x, t = q.popleft()

    if x == K :
        break

    for nxt in (2*x, x-1, x+1) :
        if 0 <= nxt <= 100_000 and v.get(nxt, 1e9) > t+1 :
            q.append((nxt, t+1))
            v[nxt] = t+1

print(t)