import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
size = max(100000, max(N, K)*2) + 1
visited = [False] * size
queue = deque([(N, 0)])
visited[N] = True 

while queue :
    cur, elapse = queue.popleft()
    if cur == K :
            print(elapse)
            break
    for next in [2*cur, cur+1, cur-1] :
        if 0 <= next <= size-1 and not visited[next] :
            queue.append((next, elapse+1))
            visited[next] = True
        
