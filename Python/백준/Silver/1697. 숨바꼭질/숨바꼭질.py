from collections import deque
N, K = map(int, input().split())
size = 100001
visited = [False] * size
queue = deque([(N, 0)])
visited[N] = True 

while queue :
    cur, elapse = queue.popleft()
    if cur == K :
            print(elapse)
            break
    for next in [cur+1, cur-1, 2*cur] :
        if 0 <= next <= size-1 and not visited[next] :
            queue.append((next, elapse+1))
            visited[next] = True
        
